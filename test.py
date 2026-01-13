import logging
logging.basicConfig(format='%(asctime)s [%(levelname)-8s] %(name)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

from resonitelink import ResoniteLinkClient, ResoniteLinkClientEvent
from resonitelink.json import ResoniteLinkJSONEncoder, ResoniteLinkJSONDecoder, format_object_structure
from resonitelink.models.datamodel import Slot, Component, Reference, Field, Field_String
from resonitelink.models.messages import RemoveSlot, GetSlot, AddSlot, AddComponent, ImportTexture2DRawData
from random import randint
from typing import List
import asyncio
import json

logger = logging.getLogger("App")
logger.setLevel(logging.DEBUG)


# port = int(input("ResoniteLink Port: "))
port = 33296


def test_generate_image_bytes() -> bytes:
    data : List[int] = []

    for x in range(16):
        for y in range(16):
            data.append(x * 16)
            data.append(y * 16)
            data.append(255)
            data.append(255)
    
    return bytes(data)


async def on_client_started(client : ResoniteLinkClient):
    new_slot_id = f"RLPY_{randint(10000000, 99999999)}"

    msg = AddSlot(data=Slot(id=new_slot_id, parent=Slot.Root, name=Field_String(value="My awesome slot!!!")))
    response = await client.send_message(msg)

    logger.info(f"Received response:\n   {'\n   '.join(format_object_structure(response, print_missing=True).split('\n'))}")

    # for component_type in [ 
    #     "[FrooxEngine]FrooxEngine.ValueField<bool>", 
    #     # "[FrooxEngine]FrooxEngine.ValueField<int>", 
    #     # "[FrooxEngine]FrooxEngine.ValueField<string>" 
    # ]:
    #     msg = AddComponent(container_slot_id=new_slot_id, data=Component(component_type=component_type))
    #     await client.send_message(msg)
    
    # msg = AddSlot(data=Slot(parent=Reference(target_type="[FrooxEngine]FrooxEngine.Slot", target_id=new_slot_id), name=Field_String(value="Child")))
    # await client.send_message(msg)

    # msg = GetSlot(slot_id=new_slot_id, include_component_data=True)
    # await client.send_message(msg)

    # msg = ImportTexture2DRawData(width=16, height=16)
    # msg.raw_binary_payload = test_generate_image_bytes()
    # await client.send_message(msg)

client = ResoniteLinkClient(log_level=logging.DEBUG)
client.register_event_handler(ResoniteLinkClientEvent.STARTED, on_client_started) # TODO: Decorator syntax

asyncio.run(client.start(port))
