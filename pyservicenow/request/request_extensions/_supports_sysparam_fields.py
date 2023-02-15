"""Houses Supports Sysparam Fields"""

from typing import List, TypeVar, overload, Type, Callable, Generic

from pyrestsdk.request.supports_types import SupportsGenericType

from pyservicenow.types.enums import QueryParameters
from pyservicenow.types.models import ServiceNowQueryOption
from pyrestsdk.request.supports_types import SupportsQueryOptions

S = TypeVar("S", bound="SupportsSysparamFields")
T = TypeVar("T")


class SupportsSysparamFields(SupportsQueryOptions, SupportsGenericType):
    """Supports Sysparam Fields Type"""

    def sysparam_fields(self: S, fields: List[str]) -> S:
        
        self.query_options.append(
            ServiceNowQueryOption(QueryParameters.FIELDS, fields)
        )
        
        return self

    #@overload
    #def sysparam_fields(self: S, expression: Callable[[Type[T]],List[property]]) -> S:...
    
    """def sysparam_fields(self:S, *args, **kwargs) -> S:
        Adds the listed fields

        Args:
            fields (List[str]): The fields to be returned

        Returns:
            TableEntryCollectionRequest: The request object to send.
        
        fields: List[str] = []
        
        args = list(args)
        
        if len(args) > 1:
            raise Exception(f"Too many arguments, excepted 1 got {len(args)}")
        
        if len(args) == 0:
            expression = kwargs.get("expression", None)
            val =  kwargs.get("fields", expression)
            args.append(val)
            
        if isinstance(args[0], list):
            fields = args[0]
        else:
            lambda_expression = args[0]
            fields = get_properties(lambda_expression, self.generic_type)

        self.query_options.append(
            ServiceNowQueryOption(QueryParameters.FIELDS, fields)
        )
        return self"""
    
    
def  get_properties(expression: Callable[[Type[T]],List[property]], type_of: Type[T]) -> List[str]:
    
    raw_properties = expression(type_of)
    
    return [prop.fget.__name__ for prop in raw_properties]