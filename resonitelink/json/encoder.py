from .models import JSONProperty, get_model_for_data_class
from typing import Any
from json import JSONEncoder


class ResoniteLinkJSONEncoder(JSONEncoder):
    """
    Custom encoder for ResoniteLink model classes.

    """
    def default(self, o : Any):
        try:
            # Try retrieving a model to quickly check if the object to encode is a model's data class
            model = get_model_for_data_class(type(o))
        
        except KeyError:
            # Not a registered model class, forward to default encoder
            return super().default(o)
        
        else:
            # Object is data class of a model, resolve into object
            obj = { '$type': model.type_name }

            json_property : JSONProperty
            for key, json_property in model.properties.items():
                if hasattr(o, key):
                    # Object has property for key, include
                    obj[json_property.name] = getattr(o, key)
            
            return obj
