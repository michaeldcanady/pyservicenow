from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from pyservicenow.core import ServiceNowClient
from pyrestsdk.requestbuilder import EntityRequestBuilder

class BatchRequestBuilder(EntityRequestBuilder):
    
    def __init__(self, request_url: str, client: ServiceNowClient) -> None:
        super().__init__(request_url, client)

    @property
    def request(self):
        return super().request