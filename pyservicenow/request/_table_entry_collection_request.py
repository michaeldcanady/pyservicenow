from __future__ import annotations
import typing
from typing import Union, TypeVar, Type, List, Optional, Generic, TYPE_CHECKING
if TYPE_CHECKING:
    from pyservicenow.core import ServiceNowClient

# Interal Imports
from pyservicenow.types.enums import HttpsMethods, Header, MimeTypeNames
from pyservicenow.types.models import ServiceNowEntry, ServiceNowHeaderOption
from pyservicenow.request._base_table_request import BaseTableRequest
from pyservicenow.types.exceptions import UnexpectedReturnType

S = TypeVar("S", bound=ServiceNowEntry)

class TableEntryCollectionRequest(BaseTableRequest):
    """The Table Entry Collection Request
    """

    def __init__(self, request_url: str, client: 'ServiceNowClient', options) -> None:
        super().__init__(request_url, client, options)

    @property
    def Get(self) -> TableEntryCollectionRequest:

        self._headers.append(ServiceNowHeaderOption(Header.Accept, MimeTypeNames.Application.Json))
        self.Method = HttpsMethods.GET

        return self

    @property
    def Invoke(self) -> List[ServiceNowEntry]:

        return self.Send(ServiceNowEntry, None)
    
    def Send(self, obj_type: Type[S], object: Optional[S] = None) -> List[S]:

        if type(_return := super().Send(obj_type, object, None, None)) is not list:
            raise UnexpectedReturnType(type(_return), List)
        
        return _return