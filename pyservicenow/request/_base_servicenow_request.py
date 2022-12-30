from __future__ import annotations
from typing import TYPE_CHECKING, Iterable, Union, TypeVar, Type, Optional, Dict, List, Callable
if TYPE_CHECKING:
    from pyservicenow.core import ServiceNowClient

import json

from pyrestsdk.request import BaseRequest
from pyrestsdk.type.enum import HttpsMethod

# Interal Imports
from pyservicenow.types.models import ServiceNowQueryOption, ServiceNowHeaderOption, ServiceNowEntry, CollectionPage
from pyservicenow.types.enums import Header, MimeTypeNames

B = TypeVar("B", bound='BaseServiceNowEntryRequest')

S = TypeVar("S", bound='CollectionPage')

class BaseServiceNowEntryRequest(BaseRequest):

    _object: Optional[S] = None

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
    def Invoke(self: B) -> S:

        return self.Send(self._object)

    def _sendRequest(
        self, value: Optional[S]
    ) -> Optional[Dict[str, Union[List, Dict]]]:

        _request_dict: Dict[HttpsMethod, Callable] = {
            HttpsMethod.GET: self._client.get,
            HttpsMethod.POST: self._client.post,
            HttpsMethod.DELETE: self._client.delete,
            HttpsMethod.PUT: self._client.put,
        }

        #Logger.info(
        #    f"{type(self).__name__}._sendRequest: {self.Method.name} request made"
        #)

        _func = _request_dict.get(self.Method, None)

        if _func is None:
            raise Exception(f"Unknown HTTPS method {self.Method.name}")

        _response = _func(
            url=self.RequestUrl,
            params=self._query_options.asDict(),
            data=json.dumps(value.Json()) if value is not None else None,
        )

        if self.Method == HttpsMethod.DELETE:
            return None

        self._return_type.fromResponse(_response, self.Client)