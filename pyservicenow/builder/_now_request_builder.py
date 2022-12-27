from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from pyservicenow.core import ServiceNowClient
from pyrestsdk.requestbuilder import EntityRequestBuilder

# internal imports
from pyservicenow.builder._table_request_builder import TableRequestBuilder
from pyservicenow.builder._ui_request_builder import UIRequestBuilder
from pyservicenow.builder._batch_request_builder import BatchRequestBuilder

class NowRequestBuilder(EntityRequestBuilder):

    def __init__(self, request_url: str, client: ServiceNowClient) -> None:
        super().__init__(request_url, client)

    def Table(self, table_name: str) -> TableRequestBuilder:
        """Get a specific serviceNow table

        Args:
            table_name (str): table name

        Returns:
            TableRequestBuilder: The table path
        """

        return TableRequestBuilder(self.AppendSegmentToRequestUrl(f"/table/{table_name}"), self.Client)

    @property
    def Batch(self) -> BatchRequestBuilder:
        return BatchRequestBuilder(self.AppendSegmentToRequestUrl("/batch"), self.Client)
    
    @property
    def UI(self) -> UIRequestBuilder:

        return UIRequestBuilder(self.AppendSegmentToRequestUrl("ui"), self.Client)