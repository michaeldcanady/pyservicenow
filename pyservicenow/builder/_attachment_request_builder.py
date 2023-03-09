"""Houses attachment request builder"""

from __future__ import annotations

from typing import Iterable, Optional, Union, TypeVar, TYPE_CHECKING

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

from pyservicenow.builder._attachment_file_request_builder import AttachmentFileRequestBuilder

if TYPE_CHECKING:
    from pyservicenow.core import ServiceNowClient

B = TypeVar("B", bound="EntityRequestBuilder")

class AttachmentRequestBuilder(
    EntityRequestBuilder[AttachmentEntryCollectionRequest],
    AbstractAttachmentRequestBuilder,
):
    """The Attachment Request Builder type"""
    
    def __init__(self: B, request_url: str, client: ServiceNowClient) -> None:
        super().__init__(request_url, client)

    def request_with_options(
        self,
        options: Optional[
            Iterable[Union[ServiceNowQueryOption, ServiceNowHeaderOption]]
        ],
    ) -> AttachmentEntryCollectionRequest:

        return AttachmentEntryCollectionRequest(
            self.request_url, self.request_client, options
        )
        
    @property
    def file(self) -> AttachmentFileRequestBuilder:
        
        return AttachmentFileRequestBuilder(self.append_segment_to_request_url("file"), self.request_client)

    def request_by_id(self, sys_id: str) -> AttachmentEntryRequest:

        return AttachmentEntryRequest(
            self.append_segment_to_request_url(sys_id), self.request_client, None
        )
