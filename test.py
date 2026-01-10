import logging
logging.basicConfig(format='%(asctime)s [%(levelname)-8s] %(name)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

from resonitelink import ResoniteLinkClient, ResoniteLinkClientEvent
from resonitelink.json import ResoniteLinkJSONEncoder, ResoniteLinkJSONDecoder, get_model_for_data_class
from resonitelink.models.datamodel import Slot, Reference
from resonitelink.models.messages import RemoveSlot, GetSlot, AddSlot
import asyncio
import json

logger = logging.getLogger("App")
logger.setLevel(logging.DEBUG)


port = int(input("ResoniteLink Port: "))

async def on_client_started(client : ResoniteLinkClient):
    logger.info("Start event invoked!")

    msg = AddSlot()
    msg.data = Slot()
    msg.data.parent = Reference()
    msg.data.parent.target_id = "Root"
    msg.data.parent.target_type = "Slot"
    logger.info(f"Sending message: {msg}")
    await client.send_message(msg)

client = ResoniteLinkClient(log_level=logging.DEBUG)
client.register_event_handler(ResoniteLinkClientEvent.STARTED, on_client_started) # TODO: Decorator syntax

asyncio.run(client.start(port))