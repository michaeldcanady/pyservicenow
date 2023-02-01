"""Houses attachment request builder"""

from __future__ import annotations
from typing import TYPE_CHECKING, Iterable, Optional, Union
from pyrestsdk.requestbuilder import EntityRequestBuilder
from pyservicenow.types.models import (
    ServiceNowQueryOption,
    ServiceNowHeaderOption,
)
from pyservicenow.request import (
    AttachmentEntryRequest,
    AttachmentEntryCollectionRequest,
)


class AttachmentRequestBuilder(EntityRequestBuilder[AttachmentEntryCollectionRequest]):
    """The Attachment Request Builder type"""

    def request_with_options(
        self,
        options: Optional[
            Iterable[Union[ServiceNowQueryOption, ServiceNowHeaderOption]]
        ],
    ) -> AttachmentEntryCollectionRequest:
        """Constructs an Attachment Entry Collection Request

        Args:
            options (Optional[Iterable[Union[ServiceNowQueryOption, ServiceNowHeaderOption]]]):
            query or header options to include in the request

        Returns:
            AttachmentEntryCollectionRequest: The constructed Table Entry Collection Request
        """

        return AttachmentEntryCollectionRequest(self.request_url, self.request_client, options)

    def id(self, sys_id: str) -> AttachmentEntryRequest:
        """Constructs a Table Entry Requst using the provided sys_id

        Args:
            sys_id (str): Table Entry's sys_id

        Returns:
            AttachmentEntryRequest: The constructed Table Entry Request
        """

        return AttachmentEntryRequest(
            self.append_segment_to_request_url(sys_id), self.request_client, None
        )
