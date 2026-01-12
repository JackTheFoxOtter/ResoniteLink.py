from __future__ import annotations # Delayed evaluation of type hints (PEP 563)

from typing import Union, Optional, Any, Type, Tuple, List, Dict, Generator, TypeVar, Generic, ClassVar
from annotationlib import get_annotations
import logging


logger = logging.getLogger("ResoniteLinkModels")
logger.setLevel(logging.DEBUG)

_model_type_name_mapping : Dict[str, JSONModel] = {}
_model_data_class_mapping : Dict[Type, JSONModel] = {}


D = TypeVar('D', bound=Type)
class JSONModel(Generic[D]):
    """
    Descriptor class for JSON serializable "models" with "properties".
    A model is associated with a unique type name, which in JSON is represented in the "$type" parameter.
    A model is also backed by a data class, which is the class that holds the actual data of the model in the program.
    
    """
    _type_name : str
    _data_class : D
    _properties : Dict[str, JSONProperty]
    _property_name_mapping : Dict[str, str]
    
    @property
    def type_name(self) -> str:
        return self._type_name
    
    @property
    def data_class(self) -> D:
        return self._data_class
    
    @property
    def properties(self) -> Dict[str, JSONProperty]:
        return self._properties
    
    @property
    def property_name_mapping(self) -> Dict[str, str]:
        return self._property_name_mapping

    def __init__(self, type_name : str, data_class : D):
        self._type_name = type_name
        self._data_class = data_class
        self._properties = dict(self._find_properties_in_data_class(self.data_class)) # type: ignore
        self._verify_properties(self._properties)
        self._property_name_mapping = dict(self._get_property_name_mapping(self._properties))
        self._register()
    
    def _find_properties_in_data_class(self, data_class : Type) -> Generator[Tuple[str, JSONProperty], Any, Any]:
        """
        Inspects the specified data class and produces key-value pairs for all defined JSONProperties.
        Also recursively processes all base classes (if any).

        Returns
        -------
        Generator object that produces tuples for each each field annoated with JSONProperty, where tpl[0] is the annoated field name,
        and tpl[1] is the first JSONProperty found in its annotation metadata.

        """
        # TODO: Error for duplicate property names, they have to be unique!
        for base_class in data_class.__bases__:
            # If there are base classes, they will be processed recursively first
            for tpl in self._find_properties_in_data_class(base_class): yield tpl

        for key, annotation in get_annotations(data_class).items():
            if not hasattr(annotation, '__metadata__'):
                # We can skip all annotations that don't have metadata
                continue
            
            # The __metadata__ tuple contains metadata injected by typing.Annotated
            metadata = getattr(annotation, '__metadata__')

            # Find first metadata that is a JSONProperty instance (if it exists)
            json_property : Union[JSONProperty, None] = next(iter([ m for m in metadata if isinstance(m, JSONProperty) ]), None)
            
            if json_property:
                # Success! We've found a JSON property of the model class
                yield (key, json_property)
    
    def _verify_properties(self, properties : Dict[str, JSONProperty]):
        """
        Verifies the provided properties.
        This is needed as a separate step for issues that can only be detected after all properties have been passed,
        for example wether a abstract JSONProperty has not been overridden.

        """
        for key, json_property in properties.items():
            if json_property.abstract:
                # Abstract property that wasn't overridden
                raise TypeError(f"Invalid properties for JSONModel '{self}': Data class does not provide concrete implementation of abstract JSONProperty '{json_property}'!")

    
    def _get_property_name_mapping(self, properties : Dict[str, JSONProperty]) -> Generator[Tuple[str, str], Any, Any]:
        """
        Produces key-value pair mappings for each property to associate every JSONProperty's (unique) name with the
        name of the corresponding annotated field in the model's data class.

        Returns
        -------
        Generator object that produces tuples for each item in the provided properties dict, where tpl[0] is the JSONProperty's (unique) name,
        and tpl[1] is the name of the corresponding annotated field in the model's data class.

        """
        for key, json_property in properties.items():
            yield json_property.json_name, key

    def _register(self):
        """
        Registers this model by adding it to the global _model_mapping and _model_reverse_mapping dicts.
        
        Raises
        ------
        KeyError
            If a model with the same type name is already registered, or if this model instance is already registered under a different name.

        """
        global _model_type_name_mapping
        global _model_data_class_mapping

        if self.type_name in _model_type_name_mapping.keys():
            raise KeyError(f"A different model with type name '{self.type_name}' is already registered!")
        if self.data_class in _model_data_class_mapping.keys():
            raise KeyError(f"A different model with data class '{self.data_class}' is already registered!")
        if self in _model_type_name_mapping.values():
            raise KeyError(f"This model instance is already registered under a different type name!")
        
        logger.debug(f"Registering JSONModel '{self.type_name}' with data class '{self.data_class}':")
        if len(self.properties) == 0:
            logger.debug(f"  -> No fields annotated with JSONProperty found!")
            logger.warning(f"Data class '{self.data_class}' of JSONModel '{self.type_name}' has no fields annotated with JSONProperty!")
        else:
            for key, json_property in self.properties.items():
                logger.debug(f"  -> '{key}': {json_property}")
        
        _model_type_name_mapping[self.type_name] = self
        _model_data_class_mapping[self.data_class] = self # type: ignore
    
    def __repr__(self) -> str:
        return f"<JSONModel type_name='{self.type_name}', data_class='{self.data_class}', property_count={len(self.properties)}>"


def get_model_for_data_class(data_class : Type) -> JSONModel:
    """
    Returns the model instance registered for the provided data class.

    Parameters
    ----------
    data_class : Type
        The type of the requested model's data class.
    
    Returns
    -------
    The JSONModel associated with this data class.

    Raises
    ------
    KeyError
        If there is no registered model with the specified data class.

    """
    global _model_data_class_mapping

    return _model_data_class_mapping[data_class]


def get_model_for_type_name(type_name : str) -> JSONModel:
    """
    Returns the model instance registered for the provided type name.

    Parameters
    ----------
    type_name : str
        The type name of the requested model.

    Returns
    -------
    The JSONModel associated with this type name.

    Raises
    ------
    KeyError
        If there is no registered model with the specified type name.

    """
    global _model_type_name_mapping

    return _model_type_name_mapping[type_name]


def json_model(type_name : str):
    """
    Class decorator to easily declare models from their data classes.
    This decorator does **not** modify the decorated class, but globally registers a model for it.

    Parameters
    ----------
    type_name : str
        The model type name to associate the decorated data class with.
        (This will be used by JSON serializer / deserializer as the '$type' value.)

    """
    def _model_decorator(data_class : D) -> D:
        # Creating a model instance automatically registers it
        model = JSONModel(type_name=type_name, data_class=data_class)

        # Inject custom __repr__
        def _repr(self) -> str:
            return f"<{data_class.__name__} (data class for JSONModel '{model.type_name}')>"

        setattr(data_class, '__repr__', _repr)

        # Return decorated class again
        return data_class

    return _model_decorator


class JSONProperty():
    """
    Denotes a JSON property of a model data class that will be picked up by the serializer / deserializer.
    This should be added as an annotation to the members that should be JSON serialized / deserialized:
        
        @model("example")
        def ExampleModel():
            example_str : typing.Annotated[str, JsonProperty("exampleStr")]
            example_int : typing.Annotated[int, JsonProperty("exampleInt")]
    
    """
    _json_name : str
    _model_type_name : Optional[str]
    _abstract : bool

    @property
    def json_name(self) -> str:
        return self._json_name

    @property
    def model_type_name(self) -> Optional[str]:
        return self._model_type_name

    @property
    def abstract(self) -> bool:
        return self._abstract

    def __init__(self, json_name : str, model_type_name : Optional[str] = None, abstract = False):
        """
        Defines a new JSONProperty.

        Parameters
        ----------
        name : str
            The name of this property in JSON objects.
        model_type_name : str (optional)
            The child model's `type_name` if this property can hold a different JSON model's data. This is used to 
            identify 'anonymous' model objects during decoding of JSON data, those models don't specify an explit `$type` 
            parameter, since their type is implicitly defined through the type of their field in the parent object.
        abstract : bool (default=False)
            Whether this property is "abstract" and needs to be overridden by a implementing class. If a `JSONModel` with
            an abstract `JSONProperty` is created, a `TypeError` will be raised.

        """
        self._json_name = json_name
        self._model_type_name = model_type_name
        self._abstract = abstract
    
    def __repr__(self) -> str:
        return f"<JSONProperty name='{self.json_name}{f', model_type_name:{self._model_type_name}' if self._model_type_name else ''}{' (abstract)' if self._abstract else ''}'>"
