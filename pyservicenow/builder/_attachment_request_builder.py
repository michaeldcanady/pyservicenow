from __future__ import annotations
from typing import TYPE_CHECKING, Iterable, Optional, Union

if TYPE_CHECKING:
    from pyservicenow.core import ServiceNowClient

from pyrestsdk.requestbuilder import EntityRequestBuilder

from pyservicenow.types.models import (
    ServiceNowQueryOption,
    ServiceNowHeaderOption,
)

from pyservicenow.request import (
    AttachmentEntryRequest,
    AttachmentEntryCollectionRequest,
)


class AttachmentRequestBuilder(EntityRequestBuilder):
    """The Table Request Builder type"""

    @property
    def request(self) -> AttachmentEntryCollectionRequest:
        """Constructs a Table Entry Collection Request

        Returns:
            AttachmentEntryCollectionRequest: The constructed Table Entry Collection Request
        """

        return self.Request(None)

    def Request(
        self,
        options: Optional[
            Iterable[Union[ServiceNowQueryOption, ServiceNowHeaderOption]]
        ],
    ) -> AttachmentEntryCollectionRequest:
        return AttachmentEntryCollectionRequest(self.RequestUrl, self.Client, options)

    def id(self, sys_id: str) -> AttachmentEntryRequest:
        """Constructs a Table Entry Requst using the provided sys_id

        Args:
            sys_id (str): Table Entry's sys_id

        Returns:
            AttachmentEntryRequest: The constructed Table Entry Request
        """

        return AttachmentEntryRequest(
            self.AppendSegmentToRequestUrl(sys_id), self.Client, None
        )
