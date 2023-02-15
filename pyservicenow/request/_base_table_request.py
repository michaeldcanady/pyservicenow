"""Houses Base Table Request"""

from __future__ import annotations
from typing import TypeVar, overload, List, Type, Callable
from pyservicenow.request.request_extensions import (
    SupportsDisplayValue,
    SupportsExcludeReferenceLink,
    SupportsNoCount,
    SupportsNoDomain,
    SupportsSuppressPaginationHeader,
    SupportsSysparamCategory,
    SupportsSysparamFields,
    SupportsSysparamLimit,
    SupportsSysparamOffset,
    SupportsSysparamQuery,
    SupportsSysparamView,
)
from pyservicenow.request._base_servicenow_request import BaseServiceNowEntryRequest
from pyservicenow.types.models import (
    ServiceNowEntry,
)

S = TypeVar("S", bound=ServiceNowEntry)
T = TypeVar("T", bound=SupportsSysparamFields)


class BaseTableRequest(
    SupportsSysparamOffset,
    SupportsSysparamLimit,
    SupportsSysparamQuery,
    SupportsExcludeReferenceLink,
    SupportsDisplayValue,
    SupportsSysparamFields,
    SupportsNoCount,
    SupportsSysparamCategory,
    SupportsNoDomain,
    SupportsSuppressPaginationHeader,
    SupportsSysparamView,
    BaseServiceNowEntryRequest[S],
):
    """Base Table Request types"""

    def __init__(self: T, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    @overload
    def sysparam_fields(self: T, fields: List[str]) -> T:
        ...

    @overload
    def sysparam_fields(self: T, expression: Callable[[Type[S]],List[property]]) -> T:
        ...

    def sysparam_fields(self: T, *args, **kwargs) -> T:
        
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
        
        return super().sysparam_fields(fields)

def  get_properties(expression: Callable[[Type[T]],List[property]], type_of: Type[T]) -> List[str]:
    
    raw_properties = expression(type_of)
    
    return [prop.fget.__name__ for prop in raw_properties]