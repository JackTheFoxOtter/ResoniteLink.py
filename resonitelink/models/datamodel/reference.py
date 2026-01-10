from resonitelink.models.datamodel import Member
from resonitelink.json.models import JSONProperty, json_model
from typing import Annotated


@json_model("reference")
class Reference(Member):
    target_id : Annotated[str, JSONProperty("targetId")]
    target_type : Annotated[str, JSONProperty("targetType")]