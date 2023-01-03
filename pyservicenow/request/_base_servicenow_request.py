from __future__ import annotations
from typing import TYPE_CHECKING, Iterable, Union, TypeVar, Type, Optional, List, Dict
if TYPE_CHECKING:
    from pyservicenow.core import ServiceNowClient
    
from requests import Response

from pyrestsdk.request import BaseRequest
from pyrestsdk.type.enum import HttpsMethod

# Interal Imports
from pyservicenow.types.models import ServiceNowQueryOption, ServiceNowHeaderOption, ServiceNowEntry
from pyservicenow.types.enums import Header, MimeTypeNames

B = TypeVar("B", bound="BaseServiceNowEntryRequest")
S = TypeVar("S", bound="ServiceNowEntry")


class BaseServiceNowEntryRequest(BaseRequest):

    def __init__(self, _return_type: Type[S], request_url: str, client: 'ServiceNowClient', options: Iterable[Union[ServiceNowQueryOption, ServiceNowHeaderOption]]) -> None:
        super().__init__(_return_type, request_url, client, options)

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

    def Delete(self: B) -> B:

        self._headers.append(ServiceNowHeaderOption(Header.Accept, MimeTypeNames.Application.Json))
        self.Method = HttpsMethod.DELETE
        self._object = None

        return self

    def Put(self: B, input_object: S) -> B:

        self._headers.append(ServiceNowHeaderOption(Header.Accept, MimeTypeNames.Application.Json))
        self.Method = HttpsMethod.PUT
        self._object = input_object

        return self
    
    def parse_response(self, _response: Optional[Response]) -> Optional[Union[List[S], S]]:
        
        if _response is None:
            return None
        
        _parse_dict = {
            list: parse_result_list,
            dict: parse_result
        }
        
        _json = _response.json()
        _result = _json["result"]
        del _json
        
        _func = _parse_dict.get(type(_result), None)
        
        if _func is None:
            raise Exception(f"Unknown type {type(_result)}")
        
        return _func(self._return_type, _result, self.Client)
        
    @property
    def Invoke(self: B) -> S:

        return self.Send(self._object)
    
def parse_result(obj_type: Type[S], result: Dict, client) -> S:
    return obj_type.fromJson(result, client)


def parse_result_list(obj_type: Type[S], results: List, client) -> List[S]:
    _results: List[S] = []

    for raw_result in results:
        _entry = obj_type.fromJson(raw_result, client)
        _entry.__client = client
        _results.append(_entry)

    return _results