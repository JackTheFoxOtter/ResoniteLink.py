from resonitelink.models.assets.mesh import TriangleSubmeshRawData 
from resonitelink.models.datamodel import Float3, Color, Reference, SyncList, Field_Enum, Field_Float, Field_Uri
from resonitelink import ResoniteLinkClient, ResoniteLinkWebsocketClient
from typing import Tuple, List, Generator, Any
from math import sin, cos
import asyncio


# Creates a new client that connects to ResoniteLink via websocket.
client = ResoniteLinkWebsocketClient()


@client.on_started
async def on_client_started(client : ResoniteLinkClient):
    """
    This async function is called by the client at the end of its startup sequence.
    You can use it to execute code once the client is up and running!

    """
    def generate_wave_grid_points(
        grid_resolution : Tuple[int, int], 
        grid_scale : Tuple[float, float, float], 
        wave_scale : Tuple[float, float] = (1.0, 1.0), 
        wave_offset : Tuple[float, float] = (0.0, 0.0)
    ) -> List[Float3]:
        """
        Generates a grid of points, where the y offset of each point is determined through a wave function.

        Parameters
        ----------
        grid_resolution : Tuple[int, int]
            The X and Z resolution of the grid.
        grid_scale : Tuple[float, float, float]
            Scaling factor for the X, Y and Z dimensions.
        wave_scale : Tuple[float, float]
            X and Z scale for the wave function.
        wave_offset : Tuple[float, float]
            X and Z offset for the wave function.
        
        Returns
        -------
        List of grid points as Float3s.

        """
        def _generate() -> Generator[Float3, Any, Any]:
            for x in range(grid_resolution[0]):
                for z in range(grid_resolution[1]):
                    y = sin(x * wave_scale[0] + wave_offset[0]) * cos(z * wave_scale[1] + wave_offset[1])
                    yield Float3(x * grid_scale[0], y * grid_scale[1], z * grid_scale[2])
        
        return list(_generate())

    def generate_grid_colors(grid_resolution : Tuple[int, int]) -> List[Color]:
        """
        Returns a list of colors for every point in a grid, mapping X and Z to R and G.

        Parameters
        ----------
        grid_resolution : Tuple[int, int]
            Size of the grid.
        
        Returns
        -------
        List of colors for each point of the grid.

        """
        def _generate() -> Generator[Color, Any, Any]:
            for x in  range(grid_resolution[0]):
                for y in range(grid_resolution[1]):
                    r = x / (grid_resolution[0] - 1)
                    g = y / (grid_resolution[1] - 1)
                    b = 0.0
                    a = 1.0
                    yield Color(r, g, b, a)
        
        return list(_generate())

    def triangulate_grid(grid_resolution : Tuple[int, int], points : List[Float3]) -> List[int]:
        """
        Simple triangulation algorithm for a grid of points.

        Parameters
        ----------
        grid_resolution : Tuple[int, int]
            The X and Z resolution of the grid.
        points : List[Float3]
            List of points in the grid.
        
        Returns
        -------
        List of triangle indices, defining the three points of each triangle.

        """
        if len(points) != grid_resolution[0] * grid_resolution[1]:
            raise ValueError("Invalid point count for grid size!")
        
        def _generate() -> Generator[int, Any, Any]:
            for x in range(grid_resolution[0] - 1):
                for y in range(grid_resolution[1] - 1):
                    # for each quad
                    idx_0 = (x)     + (y)     * grid_resolution[0]
                    idx_1 = (x + 1) + (y)     * grid_resolution[0]
                    idx_2 = (x)     + (y + 1) * grid_resolution[0]
                    idx_3 = (x + 1) + (y + 1) * grid_resolution[0]

                    yield idx_0
                    yield idx_1
                    yield idx_2

                    yield idx_2
                    yield idx_1
                    yield idx_3

        return list(_generate())
    
    def compute_normals(points : List[Float3], triangle_indices : List[int]) -> List[Float3]:
        """
        Computes vertex normals for a list of points and triangles.
        The vertex normals are defined by the average of each connected face normal (smooth shading).

        Parameters
        ----------
        points : List[Float3]
            The points of the mesh.
        triangle_indices : List[int]
            The triangle indices of the mesh.
        
        Returns
        -------
        List of normal vectors per point as Float3s.

        """
        if len(triangle_indices) % 3 != 0:
            raise ValueError("Length of triangles list must be a multiple of 3!")
        
        # Lists of normals of connected faces for each point
        connecting_face_normals : List[List[Float3]] = [ list() for point in points ]

        for i in range(0, len(triangle_indices), 3):
            idx0 = triangle_indices[i]
            idx1 = triangle_indices[i + 1]
            idx2 = triangle_indices[i + 2]
            
            p0 = points[idx0]
            p1 = points[idx1]
            p2 = points[idx2]

            a = p1 - p0
            b = p2 - p0
            n = a.cross(b)

            connecting_face_normals[idx0].append(n)
            connecting_face_normals[idx1].append(n)
            connecting_face_normals[idx2].append(n)

        return [ Float3.avg(*normals).normalized() for normals in connecting_face_normals ]
    
    grid_size = (100, 100)
    wave_scale = (0.2, 0.2)
    wave_offset = (0.0, 0.0)
    
    # Compute the mesh data.
    points = generate_wave_grid_points(grid_size, (0.01, 0.05, 0.01), wave_scale, wave_offset)
    triangle_indices = triangulate_grid(grid_size, points)
    triangle_count = int(len(triangle_indices) / 3)
    normals = compute_normals(points, triangle_indices)
    colors = generate_grid_colors(grid_size)

    # Import the mesh data into Resonite.
    asset_url = await client.import_mesh_raw_data(
        positions=points,
        normals=normals,
        colors=colors,
        submeshes=[ TriangleSubmeshRawData(triangle_count, triangle_indices) ]
    )

    # Adds a new slot. Since no parent was specified, it will be added to the world root by default.
    slot = await client.add_slot(name="Mesh Slot", position=Float3(0, 1.5, 0))

    # Adds a StaticMesh component to the slot and assigns the asset URI of the imported mesh data. 
    static_mesh = await slot.add_component(
        "[FrooxEngine]FrooxEngine.StaticMesh", 
        URL=Field_Uri(asset_url)
    )

    # Adds a PBS_VertexColorMetallic material.
    material = await slot.add_component(
        "[FrooxEngine]FrooxEngine.PBS_VertexColorMetallic", 
        Culling=Field_Enum("Off", "[FrooxEngine]FrooxEngine.Culling"),
        Smoothness=Field_Float(0.0)
    )

    # Creates a mesh renderer for the mesh and material.
    mesh_renderer = await slot.add_component(
        "[FrooxEngine]FrooxEngine.MeshRenderer", 
        Mesh=Reference(target_type="[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Mesh>", target_id=static_mesh.id),
        Materials=SyncList(Reference(target_type="[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Material>", target_id=material.id))
    )

    # Little hack to fix issue with Materials not being set currently, should be obsolete once SyncList bugs are fixed in ResoniteLink.
    await mesh_renderer.update_members(Materials=SyncList(Reference(target_type="[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Material>", target_id=material.id)))

    # Adds MeshCollider component.
    await slot.add_component("[FrooxEngine]FrooxEngine.MeshCollider")

    # Adds Grabbable component and makes it scalable.
    await slot.add_component("[FrooxEngine]FrooxEngine.Grabbable")

    # Stops the client manually. Without this, the client will run forever, which might be desired for some use-cases.
    await client.stop()


# Start the client, it will automatically connect to the first ResoniteLink session it discovers on the local network.
asyncio.run(client.start(auto_discover=True))
