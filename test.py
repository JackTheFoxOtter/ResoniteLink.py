from resonitelink.json import *
from resonitelink.math import VectorBase
from resonitelink.types import *
from resonitelink import *
from resonitelink.models.system.resonite_link_session import ResoniteLinkSession
from typing import List, Tuple, Union, Type
from abc import ABC, abstractmethod
import asyncio
import logging

from resonitelink.types import *
from resonitelink.utils.session_listener import *
from numpy.typing import NDArray


from resonitelink.models.assets.mesh import TriangleSubmeshRawData 
from resonitelink.models.datamodel import Float3, Color, Reference, SyncList, Field_Enum, Field_Float, Field_Uri
from resonitelink import ResoniteLinkClient, ResoniteLinkWebsocketClient
from typing import Tuple, List, Generator, Any
from math import sin, cos, sqrt
import asyncio
import numpy as np


# v1 = Float3(100.0, 0.0, 0.0)
# v2 = Float3(0.0, 50.0, 50.0)
# v3 = Float3(50.0, 50.0, 50.0)

# avg = Float3.avg(v1, v2, v3)
# print(f"Average: {avg}")

# v1 = Float3(1.0, 2.0, 3.0)
# v2 = Float3(0.5, 0.5, 0.5)

# print(f"Mul Vector: {v1 * v2}")
# print(f"Mul Scalar: {v1 * 0.5}")

# v1 = Float3(0, 0, 0)
# print(f"Magnitude: {v1.magnitude()}")
# print(f"Norm: {v1.normalized()}")

# m1 = Float2x2(1.0, 2.0, 3.0, 4.0)
# m2 = Float2x2(0.5, 0.5, 0.5, 0.5)
# print(f"Mul Matrix: {m1 * m2}")
# print(f"Mul Scalar: {m1 * 0.5}")

# q1 = FloatQ(0.0, 0.5, 0.25, 1.0)
# q2 = FloatQ(0.25, 0.5, 0.0, 1.0)
# print(f"Quaternion: {q1 * q2}")


from resonitelink.utils.slot_hierarchy import SlotHierarchy
from typing import Optional


# Creates a new client that connects to ResoniteLink via websocket.
client = ResoniteLinkWebsocketClient()


@client.on_started
async def on_client_started(client : ResoniteLinkClient):
    """
    This async function is called by the client at the end of its startup sequence.
    You can use it to execute code once the client is up and running!

    """
    # Fetch the ENTIRE scene
    world_root = await client.get_slot("Root", depth=-1, include_component_data=True)
    world_hierarchy = SlotHierarchy.from_slot(world_root)
    print(f"Slot {world_root.name.value}, Total Slots: {world_hierarchy.children_count_recursive + 1}, Total Components: {world_hierarchy.component_count_recursive}")

    # lizzy_slot : Optional[Slot] = None

    # for child_slot in world_root.children:
    #     if child_slot.name.value.startswith("L¡zzy Client"):
    #     # if child_slot.name.value.startswith("Test"):
    #         lizzy_slot = child_slot
    #         break
    
    # if lizzy_slot:
    #    # Lizzy found, now fully resolve this slot
    #    lizzy_slot_full = await client.get_slot(lizzy_slot, depth=-1, include_component_data=True)
    #    lizzy_hierarchy = SlotHierarchy.from_slot(lizzy_slot_full)
    #    logging.info(f"Lizzy found, total slots: {lizzy_hierarchy.children_count_recursive}")

    #    for match in lizzy_hierarchy.find(lambda slot: any([any(type(member) is Field_String and member.value == "MentorRequestsInterface/LocalRequestItem" for name, member in component.members.items()) for component in slot.slot.components])):
    #        logging.info(f"Match found: {match}")
       

    # else:
    #     logging.info("Lizzy not found in world.")

    # Stops the client manually. Without this, the client will run forever, which might be desired for some use-cases.
    await client.stop()


# Start the client, it will automatically connect to the first ResoniteLink session it discovers on the local network.
asyncio.run(client.start(auto_discover=True))








# # Creates a new client that connects to ResoniteLink via websocket.
# client = ResoniteLinkWebsocketClient()


# @client.on_started
# async def on_client_started(client : ResoniteLinkClient):
#     """
#     This async function is called by the client at the end of its startup sequence.
#     You can use it to execute code once the client is up and running!

#     """
#     def calc_uv_colors(width : int, height : int) -> List[int]:
#         """
#         Generates color data for a simple UV texture (X and Y coordinates mapped to R and G).

#         Parameters
#         ----------
#         width : int
#             Width of the texture.
#         height : int
#             Height of the texture.

#         Returns
#         -------
#         List of RGBA integer values between 0 and 255 (`byte`).

#         """
#         def _generate() -> Generator[int]:
#             for x in range(width):
#                 for y in range(height):
#                     yield int(x / width * 255)
#                     yield int(y / height * 255)
#                     yield 0
#                     yield 255

#         return list(_generate())
    
#     # Imports the color data as a texture.
#     texture_uri = await client.import_texture_2d_raw_data(
#         width=1024,
#         height=1024,
#         data=calc_uv_colors(1024, 1024)
#     )

#     # Adds a new slot. Since no parent was specified, it will be added to the world root by default.
#     slot = await client.add_slot(name="Imported Texture", position=Float3(0, 1.5, 0))

#     # Adds a Texture2DComponent, assigns a reference to the imported texture, and sets up some configuration.
#     static_texture_2d = await slot.add_component(
#         "[FrooxEngine]FrooxEngine.StaticTexture2D", 
#         URL=Field_Uri(texture_uri),
#         WrapModeU=Field_Enum("Clamp", "[FrooxEngine]FrooxEngine.TextureWrapMode"),
#         WrapModeV=Field_Enum("Clamp", "[FrooxEngine]FrooxEngine.TextureWrapMode"),
#         CrunchCompressed=Field_Bool(False),
#         MipMaps=Field_Bool(False)
#     )
    
#     # Adds an UnlitMaterial and assigns the texture.
#     material = await slot.add_component(
#         "[FrooxEngine]FrooxEngine.UnlitMaterial",
#         Texture=Reference(static_texture_2d.id, "[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>"),
#         Sidedness=Field_Enum("Double", "[FrooxEngine]FrooxEngine.Sideness")
#     )
    
#     # Adds a quad mesh to render the texture on.
#     quad_mesh = await slot.add_component("[FrooxEngine]FrooxEngine.QuadMesh")
    
#     # Creates a mesh renderer for the mesh and material.
#     mesh_renderer = await slot.add_component(
#         "[FrooxEngine]FrooxEngine.MeshRenderer", 
#         Mesh=Reference(target_type="[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Mesh>", target_id=quad_mesh.id),
#         Materials=SyncList(Reference(target_type="[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Material>", target_id=material.id))
#     )

#     # Little hack to fix issue with Materials not being set currently, should be obsolete once SyncList bugs are fixed in ResoniteLink.
#     await mesh_renderer.update_members(Materials=SyncList(Reference(target_type="[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Material>", target_id=material.id)))

#     # Adds MeshCollider component.
#     await slot.add_component("[FrooxEngine]FrooxEngine.MeshCollider")
    
#     # Adds Grabbable component and makes it scalable.
#     await slot.add_component(
#         "[FrooxEngine]FrooxEngine.Grabbable", 
#         Scalable=Field_Bool(True)
#     )

#     # Stops the client manually. Without this, the client will run forever, which might be desired for some use-cases.
#     await client.stop()


# # Start the client, it will automatically connect to the first ResoniteLink session it discovers on the local network.
# asyncio.run(client.start(auto_discover=True))










# # Creates a new client that connects to ResoniteLink via websocket.
# client = ResoniteLinkWebsocketClient(log_level=logging.INFO)

# @client.on_started
# async def on_client_started(client : ResoniteLinkClient):
#     """
#     This async function is called by the client at the end of its startup sequence.
#     You can use it to execute code once the client is up and running!

#     """
#     parent = await client.add_slot("Root", name="Lib Perf Test")
#     count = 10

#     # Test 1: Sequential
#     # for i in range(count):
#     #     await client.add_slot(parent, name=f"Child {i}")

#     # Test 2: Parallel
#     tasks = [ client.add_slot(parent, name=f"Child {i}") for i in range(count) ]
#     await asyncio.gather(*tasks)

#     # Stops the client manually. Without this, the client will run forever, which might be desired for some use-cases.
#     await client.stop()


# # Start the client on the specified port.
# asyncio.run(client.start(auto_discover=True))









# from resonitelink.utils.slot_hierarchy import SlotHierarchy
# from resonitelink.models.datamodel import Member, SyncObject, SyncList
# from resonitelink.json import json_model, json_element, format_object_structure
# from resonitelink import ResoniteLinkClient, ResoniteLinkWebsocketClient, ImportAudioClipRawData, Float3, Member, Array_Float, Array_Float3, Field_Float
# from dataclasses import dataclass
# from typing import List
# from math import pi, sin
# import asyncio
# import logging
# from array import array


# # Creates a new client that connects to ResoniteLink via websocket.
# client = ResoniteLinkWebsocketClient(log_level=logging.DEBUG)


# @client.on_started
# async def on_client_started(client : ResoniteLinkClient):
#     """
#     This async function is called by the client at the end of its startup sequence.
#     You can use it to execute code once the client is up and running!

#     """
#     # Adds a new slot. Since no parent was specified, it will be added to the world root by default.
#     # slot = await client.add_slot(name="Test Ref Slot", position=Float3(0, 1.5, 0))

#     # ref_slot_id = 'RLPY_47AB_01_0'
#     # ref_slot = await client.get_slot(ref_slot_id, -1, True)
#     # format_object_structure(ref_slot)

#     slot = await client.add_slot(name="", position=Float3(0, 1.5, 0))

#     positions : List[Float3] = []
#     scales : List[float] = []

#     resolution = 100
#     for i in range(resolution):
#         x = i / resolution
#         y = sin(2 * pi * x)

#         positions += [ Float3(x, 0, y) ]
#         scales += [ 0.01 ]

#     multi_line_mesh = await client.add_component(
#         slot, 
#         component_type="[FrooxEngine]FrooxEngine.MultiLineMesh",
#         Lines=SyncList(
#             SyncObject(
#                 Scale=Field_Float(value=0.2),
#                 Positions=Array_Float3(values=positions),
#                 Scales=Array_Float(values=scales)
#             )
#         )
#     )
    
#     line_update_data = SyncObject(
#         Scale=Field_Float(value=0.2),
#         Positions=Array_Float3(values=positions),
#         Scales=Array_Float(values=scales)
#     )

#     await client.update_component(multi_line_mesh, Lines=SyncList(line_update_data))

#     root_slot = await client.get_slot("Root", -1, False)
#     root_hierarchy = SlotHierarchy.from_slot(root_slot)
#     target_hierarchy = next(root_hierarchy.find(lambda h: h.slot.name.value == 'MultiLineMeshTest'))

#     await client.get_slot(target_hierarchy.slot, -1, True)


# # Asks for the current port ResoniteLink is running on.
# # port = int(input("ResoniteLink Port: "))
# port = 41634


# # Start the client on the specified port.
# asyncio.run(client.start(port))
