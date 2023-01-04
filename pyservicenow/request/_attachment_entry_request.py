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
from pyservicenow.types.exceptions import UnexpectedReturnType

A = TypeVar("A", bound=AttachmentEntry)
B = TypeVar("B", bound="AttachmentEntryRequest")


class AttachmentEntryRequest(BaseAttachmentRequest[AttachmentEntry]):
    def __init__(
        self,
        request_url: str,
        client: "ServiceNowClient",
        options: Optional[Iterable[Union[ServiceNowQueryOption, ServiceNowHeaderOption]]],
    ) -> None:
        super().__init__(request_url, client, options)


    @property
    def Invoke(self: B) -> AttachmentEntry:
        
        _return = super().Invoke
        
        if type(_return) is not self.GenericType:
            raise UnexpectedReturnType(type(_return), self.GenericType)
        
        return _return