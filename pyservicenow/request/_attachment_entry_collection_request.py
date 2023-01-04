from __future__ import annotations
from typing import Union, TypeVar, Iterable, TYPE_CHECKING, List, Optional

if TYPE_CHECKING:
    from pyservicenow.core import ServiceNowClient

# Interal Imports
from pyservicenow.request._base_attachment_request import BaseAttachmentRequest
from pyservicenow.types.models import (
    ServiceNowQueryOption,
    ServiceNowHeaderOption,
    AttachmentEntry,
)

from pyservicenow.types.exceptions import UnexpectedReturnType

T = TypeVar("T", bound="BaseAttachmentRequest")
A = TypeVar("A", bound=AttachmentEntry)
B = TypeVar("B", bound="AttachmentEntryCollectionRequest")


class AttachmentEntryCollectionRequest(BaseAttachmentRequest[AttachmentEntry]):
    def __init__(
        self,
        request_url: str,
        client: "ServiceNowClient",
        options: Optional[Iterable[Union[ServiceNowQueryOption, ServiceNowHeaderOption]]],
    ) -> None:
        super().__init__(request_url, client, options)
    
    @property
    def Invoke(self: B) -> List[AttachmentEntry]:
        
        _return = super().Invoke
        
        if type(_return) is not List:
            raise UnexpectedReturnType(type(_return), List[AttachmentEntry])
        
        return _return