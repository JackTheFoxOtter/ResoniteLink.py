import logging
logging.basicConfig(format='%(asctime)s [%(levelname)-8s] %(name)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

from resonitelink import ResoniteLinkClient, ResoniteLinkClientEvent
from resonitelink.json import ResoniteLinkJSONEncoder, ResoniteLinkJSONDecoder, get_model_for_data_class
from resonitelink.models.datamodel import Slot, Reference, Field
from resonitelink.models.messages import RemoveSlot, GetSlot, AddSlot
import asyncio
import json

logger = logging.getLogger("App")
logger.setLevel(logging.DEBUG)


# port = int(input("ResoniteLink Port: "))
port = 30672

async def on_client_started(client : ResoniteLinkClient):
    msg = AddSlot(data=Slot(id="RLPY_01", parent=Slot.Root))
    await client.send_message(msg)

    msg = GetSlot(slot_id="RLPY_01")
    await client.send_message(msg)

client = ResoniteLinkClient(log_level=logging.DEBUG)
client.register_event_handler(ResoniteLinkClientEvent.STARTED, on_client_started) # TODO: Decorator syntax

asyncio.run(client.start(port))
