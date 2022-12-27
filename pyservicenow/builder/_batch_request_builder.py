from __future__ import annotations
from typing import TYPE_CHECKING, Iterable
if TYPE_CHECKING:
    from pyservicenow.core import ServiceNowClient
from pyrestsdk.requestbuilder import EntityRequestBuilder
from pyservicenow.request._batch_servicenow_request import BatchServiceNowRequest

class BatchRequestBuilder(EntityRequestBuilder):
    
    def __init__(self, request_url: str, client: ServiceNowClient) -> None:
        super().__init__(request_url, client)

    @property
    def request(self) -> BatchServiceNowRequest:
        return self.Request(None)

    def Request(self, options: Iterable) -> BatchServiceNowRequest:
        return BatchServiceNowRequest(self.RequestUrl, self.Client, options)