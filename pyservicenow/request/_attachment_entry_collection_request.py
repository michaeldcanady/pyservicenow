from __future__ import annotations
from typing import Union, TypeVar, Iterable, TYPE_CHECKING, Optional
if TYPE_CHECKING:
    from pyservicenow.core import ServiceNowClient

# Interal Imports
from pyservicenow.request._base_attachment_request import BaseAttachmentRequest
from pyservicenow.types.models import ServiceNowQueryOption, ServiceNowHeaderOption, AttachmentEntry

T = TypeVar("T", bound='BaseAttachmentRequest')

class AttachmentEntryCollectionRequest(BaseAttachmentRequest):

    def __init__(self, request_url: str, client: 'ServiceNowClient', options: Optional[Iterable[Union[ServiceNowQueryOption, ServiceNowHeaderOption]]]) -> None:
        super().__init__(AttachmentEntry, request_url, client, options)