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



# vec1 = Float3(1.0, 2.0, 3.0)
# vec2 = Float3(-7.0, 8.0, 9.0)
# vec3 = vec1.cross(vec2)
# print(type(vec3))
# print(vec3)

# Creates a new client that connects to ResoniteLink via websocket.
client = ResoniteLinkWebsocketClient(log_level=logging.INFO)

@client.on_started
async def on_client_started(client : ResoniteLinkClient):
    """
    This async function is called by the client at the end of its startup sequence.
    You can use it to execute code once the client is up and running!

    """
    parent = await client.add_slot("Root", name="Lib Perf Test")
    count = 10

    # Test 1: Sequential
    # for i in range(count):
    #     await client.add_slot(parent, name=f"Child {i}")

    # Test 2: Parallel
    tasks = [ client.add_slot(parent, name=f"Child {i}") for i in range(count) ]
    await asyncio.gather(*tasks)

    # Stops the client manually. Without this, the client will run forever, which might be desired for some use-cases.
    await client.stop()


# Start the client on the specified port.
asyncio.run(client.start(auto_discover=True))









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
