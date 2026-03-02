from resonitelink.models.datamodel import Slot, Component
from resonitelink.models.responses import Response
from resonitelink.json import MISSING, json_model, json_element


__all__ = (
    'SlotData',
    'ComponentData',
    'AssetData',
    'NewEntityID'
)


@json_model("slotData", Response)
class SlotData(Response):
    depth : int = json_element("depth", int, default=MISSING)
    data : Slot = json_element("data", Slot, default=MISSING)


@json_model("componentData", Response)
class ComponentData(Response):
    data : Component = json_element("data", Component, default=MISSING)


@json_model("assetData", Response)
class AssetData(Response):
    asset_url : str = json_element("assetURL", str, default=MISSING)

@json_model("newEntityId", Response)
class NewEntityID(Response):
    entity_id : str = json_element("entityId", str, default=MISSING)