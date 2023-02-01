"""Houses attachment request builder"""

from __future__ import annotations

from typing import Iterable, Optional, Union

from pyrestsdk.requestbuilder import EntityRequestBuilder

from pyservicenow.types.models import (
    ServiceNowEntry,
    ServiceNowHeaderOption,
    ServiceNowQueryOption,
)

from pyservicenow.request import (
    ServiceNowTableEntryCollectionRequest,
)

from pyservicenow.request import TableEntryRequest


class TableRequestBuilder(EntityRequestBuilder[ServiceNowTableEntryCollectionRequest]):
    """The Table Request Builder type"""

    def request_with_options(
        self,
        options: Optional[
            Iterable[Union[ServiceNowQueryOption, ServiceNowHeaderOption]]
        ],
    ) -> ServiceNowTableEntryCollectionRequest:
        """Constructs a Table Entry Collection Request

        Args:
            options (Optional[Iterable[Union[ServiceNowQueryOption, ServiceNowHeaderOption]]]):
            query or header options to include in the request

        Returns:
            AttachmentEntryCollectionRequest: The constructed Table Entry Collection Request
        """

        return ServiceNowTableEntryCollectionRequest(
            self.request_url, self.request_client, options
        )

    def id(self, sys_id: str) -> TableEntryRequest:
        """Constructs a Table Entry Requst using the provided sys_id

        Args:
            sys_id (str): Table Entry's sys_id

        Returns:
            TableEntryRequest: The constructed Table Entry Request
        """
        return TableEntryRequest[ServiceNowEntry](
            self.append_segment_to_request_url(sys_id), self.request_client, None
        )
