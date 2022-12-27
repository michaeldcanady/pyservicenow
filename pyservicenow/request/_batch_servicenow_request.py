from __future__ import annotations
from typing import TYPE_CHECKING, Iterable, Union, TypeVar, Type, Optional
if TYPE_CHECKING:
    from pyservicenow.core import ServiceNowClient

from pyrestsdk.request import BaseRequest

# Interal Imports
from pyservicenow.request._base_servicenow_request import BaseServiceNowEntryRequest
from pyservicenow.types.models import ServiceNowQueryOption, ServiceNowHeaderOption, ServiceNowEntry
from pyservicenow.types.enums import HttpsMethods, Header, MimeTypeNames

S = TypeVar("S", bound='ServiceNowEntry')

class BatchServiceNowRequest(BaseRequest):

    def __init__(self, request_url: str, client: S, options: Iterable[Union[ServiceNowQueryOption, ServiceNowHeaderOption]]) -> None:
        super().__init__(request_url, client, options)
        self._requests = []

    def AddRequest(self, request: BaseServiceNowEntryRequest) -> None:
        self._requests.append(request)
    
    def Invoke(self):
        pass