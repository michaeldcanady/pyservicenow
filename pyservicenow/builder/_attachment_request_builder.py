"""Houses attachment request builder"""

from __future__ import annotations

from typing import Iterable, Optional, Union

from pyrestsdk.requestbuilder import EntityRequestBuilder

from pyservicenow.builder._abstract_attachment_request_builder import (
    AbstractAttachmentRequestBuilder,
)

from pyservicenow.types.models import (
    ServiceNowQueryOption,
    ServiceNowHeaderOption,
)

from pyservicenow.request import (
    AttachmentEntryRequest,
    AttachmentEntryCollectionRequest,
)


class AttachmentRequestBuilder(
    EntityRequestBuilder[AttachmentEntryCollectionRequest],
    AbstractAttachmentRequestBuilder,
):
    """The Attachment Request Builder type"""

    def request_with_options(
        self,
        options: Optional[
            Iterable[Union[ServiceNowQueryOption, ServiceNowHeaderOption]]
        ],
    ) -> AttachmentEntryCollectionRequest:

        return AttachmentEntryCollectionRequest(
            self.request_url, self.request_client, options
        )

    def id(self, sys_id: str) -> AttachmentEntryRequest:

        return AttachmentEntryRequest(
            self.append_segment_to_request_url(sys_id), self.request_client, None
        )
