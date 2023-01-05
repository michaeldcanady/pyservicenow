from __future__ import annotations
from typing import TYPE_CHECKING, Iterable, Optional, Union

if TYPE_CHECKING:
    from pyservicenow.core import ServiceNowClient

from pyrestsdk.requestbuilder import EntityRequestBuilder

# internal imports
from pyservicenow.types.models import (
    ServiceNowEntry,
    ServiceNowHeaderOption,
    ServiceNowQueryOption,
)
from pyservicenow.request._table_entry_collection_request import (
    TableEntryCollectionRequest,
)
from pyservicenow.request import TableEntryRequest


class TableRequestBuilder(EntityRequestBuilder):
    """The Table Request Builder type"""

    def __init__(self, request_url: str, client: ServiceNowClient) -> None:
        super().__init__(request_url, client)

    @property
    def request(self) -> TableEntryCollectionRequest:
        """Constructs a Table Entry Collection Request

        Returns:
            TableEntryCollectionRequest: The constructed Table Entry Collection Request
        """

        return self.Request(None)

    def Request(
        self,
        options: Optional[
            Iterable[Union[ServiceNowQueryOption, ServiceNowHeaderOption]]
        ],
    ) -> TableEntryCollectionRequest:
        return TableEntryCollectionRequest[ServiceNowEntry](
            self.RequestUrl, self.Client, None
        )

    def id(self, sys_id: str) -> TableEntryRequest:
        """Constructs a Table Entry Requst using the provided sys_id

        Args:
            sys_id (str): Table Entry's sys_id

        Returns:
            TableEntryRequest: The constructed Table Entry Request
        """

        return TableEntryRequest[ServiceNowEntry](
            self.AppendSegmentToRequestUrl(sys_id), self.Client, None
        )
