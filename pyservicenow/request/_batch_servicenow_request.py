from __future__ import annotations
from typing import TYPE_CHECKING, Iterable, Union, TypeVar, Type, Optional
if TYPE_CHECKING:
    from pyservicenow.core import ServiceNowClient

from pyrestsdk.request import BaseRequest
from pyrestsdk.type.enum import HttpsMethod

# Interal Imports
from pyservicenow.request._base_servicenow_request import BaseServiceNowEntryRequest
from pyservicenow.types.models import ServiceNowQueryOption, ServiceNowHeaderOption, ServiceNowEntry, ServiceNowRequestCollection
from pyservicenow.types.enums import Header, MimeTypeNames

S = TypeVar("S", bound='ServiceNowEntry')

class BatchServiceNowRequest(BaseRequest):

    _requests: ServiceNowRequestCollection = ServiceNowRequestCollection()

    def __init__(self, request_url: str, client: 'ServiceNowClient', options: Iterable[Union[ServiceNowQueryOption, ServiceNowHeaderOption]]) -> None:
        super().__init__(dict, request_url, client, options)

    def AddRequest(self, request: BaseServiceNowEntryRequest) -> 'BatchServiceNowRequest':

        self._requests.append(request)
        return self
    
    def Invoke(self):
        self.Method = HttpsMethod.POST

        print(self.Send(self._requests))