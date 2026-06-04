from resonitelink.models.datamodel import Reference, Float3, Field_Uri, Field_Enum, Field_Bool, SyncList
from resonitelink import ResoniteLinkClient, ResoniteLinkWebsocketClient
from typing import List, Generator
import asyncio


# Creates a new client that connects to ResoniteLink via websocket.
client = ResoniteLinkWebsocketClient()


@client.on_started
async def on_client_started(client : ResoniteLinkClient):
    """
    This async function is called by the client at the end of its startup sequence.
    You can use it to execute code once the client is up and running!

    """
    def calc_uv_colors(width : int, height : int) -> List[int]:
        """
        Generates color data for a simple UV texture (X and Y coordinates mapped to R and G).

        Parameters
        ----------
        width : int
            Width of the texture.
        height : int
            Height of the texture.

        Returns
        -------
        List of RGBA integer values between 0 and 255 (`byte`).

        """
        def _generate() -> Generator[int]:
            for x in range(width):
                for y in range(height):
                    yield int(x / width * 255)
                    yield int(y / height * 255)
                    yield 0
                    yield 255

        return list(_generate())
    
    # Imports the color data as a texture.
    texture_uri = await client.import_texture_2d_raw_data(
        width=1024,
        height=1024,
        data=calc_uv_colors(1024, 1024)
    )

    # Adds a new slot. Since no parent was specified, it will be added to the world root by default.
    slot = await client.add_slot(name="Imported Texture", position=Float3(0, 1.5, 0))

    # Adds a Texture2DComponent, assigns a reference to the imported texture, and sets up some configuration.
    static_texture_2d = await slot.add_component(
        "[FrooxEngine]FrooxEngine.StaticTexture2D", 
        URL=Field_Uri(texture_uri),
        WrapModeU=Field_Enum("Clamp", "[FrooxEngine]FrooxEngine.TextureWrapMode"),
        WrapModeV=Field_Enum("Clamp", "[FrooxEngine]FrooxEngine.TextureWrapMode"),
        CrunchCompressed=Field_Bool(False),
        MipMaps=Field_Bool(False)
    )
    
    # Adds an UnlitMaterial and assigns the texture.
    material = await slot.add_component(
        "[FrooxEngine]FrooxEngine.UnlitMaterial",
        Texture=Reference(static_texture_2d.id, "[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>"),
        Sidedness=Field_Enum("Double", "[FrooxEngine]FrooxEngine.Sideness")
    )
    
    # Adds a quad mesh to render the texture on.
    quad_mesh = await slot.add_component("[FrooxEngine]FrooxEngine.QuadMesh")
    
    # Creates a mesh renderer for the mesh and material.
    mesh_renderer = await slot.add_component(
        "[FrooxEngine]FrooxEngine.MeshRenderer", 
        Mesh=Reference(target_type="[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Mesh>", target_id=quad_mesh.id),
        Materials=SyncList(Reference(target_type="[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Material>", target_id=material.id))
    )

    # Little hack to fix issue with Materials not being set currently, should be obsolete once SyncList bugs are fixed in ResoniteLink.
    await mesh_renderer.update_members(Materials=SyncList(Reference(target_type="[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Material>", target_id=material.id)))

    # Adds MeshCollider component.
    await slot.add_component("[FrooxEngine]FrooxEngine.MeshCollider")
    
    # Adds Grabbable component and makes it scalable.
    await slot.add_component(
        "[FrooxEngine]FrooxEngine.Grabbable", 
        Scalable=Field_Bool(True)
    )

    # Stops the client manually. Without this, the client will run forever, which might be desired for some use-cases.
    await client.stop()


# Start the client, it will automatically connect to the first ResoniteLink session it discovers on the local network.
asyncio.run(client.start(auto_discover=True))
