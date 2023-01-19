"""Houses attachment request builder"""

from __future__ import annotations
from typing import TYPE_CHECKING, Iterable, Optional, Union
from pyrestsdk.requestbuilder import EntityRequestBuilder
from pyservicenow.types.models import (
    ServiceNowEntry,
    ServiceNowHeaderOption,
    ServiceNowQueryOption,
)
from pyservicenow.request._table_entry_collection_request import (
    TableEntryCollectionRequest,
)
from pyservicenow.request import TableEntryRequest

if TYPE_CHECKING:
    from pyservicenow.core import ServiceNowClient


class TableRequestBuilder(EntityRequestBuilder):
    """The Table Request Builder type"""

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
        """Constructs a Table Entry Collection Request

        Args:
            options (Optional[Iterable[Union[ServiceNowQueryOption, ServiceNowHeaderOption]]]):
            query or header options to include in the request

        Returns:
            AttachmentEntryCollectionRequest: The constructed Table Entry Collection Request
        """

        return TableEntryCollectionRequest[ServiceNowEntry](
            self.request_url, self.Client, options
        )

    def id(self, sys_id: str) -> TableEntryRequest:
        """Constructs a Table Entry Requst using the provided sys_id

        Args:
            sys_id (str): Table Entry's sys_id

        Returns:
            TableEntryRequest: The constructed Table Entry Request
        """
        return TableEntryRequest[ServiceNowEntry](
            self.append_segment_to_request_url(sys_id), self.Client, None
        )
