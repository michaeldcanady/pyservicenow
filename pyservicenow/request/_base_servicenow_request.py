from __future__ import annotations
from typing import TYPE_CHECKING, Iterable, Union, TypeVar, Type, Optional
if TYPE_CHECKING:
    from pyservicenow.core import ServiceNowClient

from pyrestsdk.request import BaseRequest

# Interal Imports
from pyservicenow.types.models import ServiceNowQueryOption, ServiceNowHeaderOption, ServiceNowEntry
from pyservicenow.types.enums import HttpsMethods, Header, MimeTypeNames

B = TypeVar("B", bound='BaseServiceNowEntryRequest')

S = TypeVar("S", bound='ServiceNowEntry')

class BaseServiceNowEntryRequest(BaseRequest):

    _object: Optional[S] = None

    def __init__(self, _return_type: Type[S], request_url: str, client: 'ServiceNowClient', options: Iterable[Union[ServiceNowQueryOption, ServiceNowHeaderOption]]) -> None:
        super().__init__(request_url, client, options)

        self._return_type = _return_type

    @property
    def Get(self: B) -> B:
        """Sets request to get request
        """
        
        self._headers.append(ServiceNowHeaderOption(Header.Accept, MimeTypeNames.Application.Json))
        self.Method = HttpsMethods.GET
        self._object = None

        return self
    
    def Post(self: B, input_object: S) -> B:

        self._headers.append(ServiceNowHeaderOption(Header.Accept, MimeTypeNames.Application.Json))
        self.Method = HttpsMethods.POST
        self._object = input_object

        return self

    def Delete(self: B, sys_id: str) -> B:

        self._headers.append(ServiceNowHeaderOption(Header.Accept, MimeTypeNames.Application.Json))
        self.Method = HttpsMethods.DELETE
        self._object = None

        return self

    def Put(self: B, input_object: S) -> B:

        self._headers.append(ServiceNowHeaderOption(Header.Accept, MimeTypeNames.Application.Json))
        self.Method = HttpsMethods.PUT
        self._object = input_object

        return self

    @property
    def Invoke(self: B) -> S:

        return self.Send(self._return_type, self._object)