from __future__ import annotations
from typing import Union, TypeVar, Iterable, TYPE_CHECKING, Type, Optional

if TYPE_CHECKING:
    from pyservicenow.core import ServiceNowClient

# Interal Imports
from pyservicenow.request._base_attachment_request import BaseAttachmentRequest
from pyservicenow.types.models import (
    ServiceNowQueryOption,
    ServiceNowHeaderOption,
    AttachmentEntry,
)

T = TypeVar("T", bound="BaseAttachmentRequest")
A = TypeVar("A", bound=AttachmentEntry)


class AttachmentEntryRequest(BaseAttachmentRequest):
    def __init__(
        self,
        return_type: Type[A],
        request_url: str,
        client: "ServiceNowClient",
        options: Optional[Iterable[Union[ServiceNowQueryOption, ServiceNowHeaderOption]]],
    ) -> None:
        super().__init__(return_type, request_url, client, options)
