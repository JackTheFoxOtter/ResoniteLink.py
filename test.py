import logging
logging.basicConfig(format='%(asctime)s [%(levelname)-8s] %(name)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

from resonitelink import ResoniteLinkClient, ResoniteLinkClientEvent
from resonitelink.json import ResoniteLinkJSONEncoder, get_model_for_data_class
from resonitelink.models import RemoveSlot, GetSlot
import asyncio
import json

logger = logging.getLogger("App")
logger.setLevel(logging.DEBUG)


get_slot = GetSlot()
get_slot.message_id = "Py_01"
get_slot.slot_id = "Py_02"
get_slot.depth = 0
get_slot.include_component_data = False

json_str = json.dumps(get_slot, cls=ResoniteLinkJSONEncoder)
logger.debug(f"JSON dumped {get_slot} -> '{json_str}'")


# port = int(input("ResoniteLink Port: "))

# async def on_client_started(client : ResoniteLinkClient):
#     logger.info("Start event invoked!")
#     await client._send_message('{"$type" : "getSlot", "slotId" : "Root", "includeComponentData" : false, "depth" : 0}')

# client = ResoniteLinkClient(log_level=logging.DEBUG)
# client.register_event_handler(ResoniteLinkClientEvent.STARTED, on_client_started) # TODO: Decorator syntax

# asyncio.run(client.start(port))