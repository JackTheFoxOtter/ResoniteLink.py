from typing import TypeVar, Generic, Type

class JSONProperty():
    """
    Denotes a JSON property of a model data class that will be picked up by the serializer / deserializer.
    This should be added as an annotation to the members that should be JSON serialized / deserialized:
        
        @model("example")
        def ExampleModel():
            example_str : typing.Annotated[str, JsonProperty("exampleStr")]
            example_int : typing.Annotated[int, JsonProperty("exampleInt")]
    
    """
    _name : str

    def __init__(self, name : str):
        self._name = name

D = TypeVar("D")
class Model(Generic[D]):
    """
    Base class for JSON serializable / deserializable models.
    
    WARNING
    ~~~~~~~
    Don't instantiate this directly. Use the `model` decorator on the data class instead.
    
    """
    _data : D


_model_mapping : dict[str, Model] = {}

def model(type : str):
    """
    Class decorator to define model classes.

    """
    def _model_decorator(data_class : Type):
        return data_class

    return _model_decorator