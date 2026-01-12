import logging
logging.basicConfig(format='%(asctime)s [%(levelname)-8s] %(name)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

from resonitelink import ResoniteLinkClient, ResoniteLinkClientEvent
from resonitelink.json import ResoniteLinkJSONEncoder, ResoniteLinkJSONDecoder
from resonitelink.models.datamodel import Slot, Component, Reference, Field
from resonitelink.models.messages import RemoveSlot, GetSlot, AddSlot, AddComponent
from random import randint
import asyncio
import json

logger = logging.getLogger("App")
logger.setLevel(logging.DEBUG)


# port = int(input("ResoniteLink Port: "))
port = 18196

async def on_client_started(client : ResoniteLinkClient):
    new_slot_id = f"RLPY_{randint(10000000, 99999999)}"

    msg = AddSlot(data=Slot(id=new_slot_id, parent=Slot.Root))
    await client.send_message(msg)

    for component_type in [ 
        "[FrooxEngine]FrooxEngine.ValueField<bool>", 
        "[FrooxEngine]FrooxEngine.ValueField<int>", 
        "[FrooxEngine]FrooxEngine.ValueField<string>" 
    ]:
        msg = AddComponent(container_slot_id=new_slot_id, data=Component(component_type=component_type))
        await client.send_message(msg)

    msg = GetSlot(slot_id=new_slot_id)
    await client.send_message(msg)

client = ResoniteLinkClient(log_level=logging.DEBUG)
client.register_event_handler(ResoniteLinkClientEvent.STARTED, on_client_started) # TODO: Decorator syntax

asyncio.run(client.start(port))
