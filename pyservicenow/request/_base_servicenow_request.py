
from __future__ import annotations
from typing import TYPE_CHECKING, Iterable, Union, TypeVar, Type, Optional, Dict, List
if TYPE_CHECKING:
    from pyservicenow.core import ServiceNowClient
import urllib.parse as urlparse
from urllib.parse import urlencode
from pyrestsdk.request import BaseRequest

# Interal Imports
from pyservicenow.types.models import ServiceNowQueryOption, ServiceNowHeaderOption, ServiceNowEntry, HeaderOptionsCollection
from pyservicenow.types.enums import Header, MimeTypeNames
from pyrestsdk.type.enum import HttpsMethod

B = TypeVar("B", bound='BaseServiceNowEntryRequest')
S = TypeVar("S", bound='ServiceNowEntry')

class BaseServiceNowEntryRequest(BaseRequest):

    _object: Optional[S] = None

    _headers: HeaderOptionsCollection = HeaderOptionsCollection()

    def __init__(self, _return_type: Type[S], request_url: str, client: 'ServiceNowClient', options: Iterable[Union[ServiceNowQueryOption, ServiceNowHeaderOption]]) -> None:
        super().__init__(_return_type, request_url, client, options)

        self._return_type = _return_type

    @property
    def Headers(self: B) -> HeaderOptionsCollection:
        return self._headers

    @property
    def Get(self: B) -> B:
        """Sets request to get request
        """
        
        self._headers.append(ServiceNowHeaderOption(Header.Accept, MimeTypeNames.Application.Json))
        self.Method = HttpsMethod.GET
        self._object = None

        return self
    
    def Post(self: B, input_object: S) -> B:

        self._headers.append(ServiceNowHeaderOption(Header.Accept, MimeTypeNames.Application.Json))
        self.Method = HttpsMethod.POST
        self._object = input_object

        return self

    def Delete(self: B, sys_id: str) -> B:

        self._headers.append(ServiceNowHeaderOption(Header.Accept, MimeTypeNames.Application.Json))
        self.Method = HttpsMethod.DELETE
        self._object = None

        return self

    def Put(self: B, input_object: S) -> B:

        self._headers.append(ServiceNowHeaderOption(Header.Accept, MimeTypeNames.Application.Json))
        self.Method = HttpsMethod.PUT
        self._object = input_object

        return self

    @property
    def Invoke(self: B) -> (List[S] | S | None):

        return self.Send(self._object)

    def asDict(self) -> Dict:

        url_parts = list(urlparse.urlparse(self.RequestUrl))
        query = dict(urlparse.parse_qsl(url_parts[4]))
        query.update(self.QueryOptions.asDict())
        url_parts[4] = urlencode(query)

        urlparse.urlunparse(url_parts)

        return {
            "headers": self.Headers.asList(),
            "url": self.RequestUrl,
            "method": self.Method
        }

    def __iter__(self) -> Iterable:

        for key, value in self.asDict().items():
            yield key, value

    def __batch__(self) -> Dict:
        return self.asDict()