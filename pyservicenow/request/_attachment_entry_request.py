"""Houses Attachment Entry Request"""

from __future__ import annotations
from typing import TypeVar
from pyservicenow.request._base_attachment_request import BaseAttachmentRequest
from pyservicenow.types.models import AttachmentEntry
from pyservicenow.types.exceptions import UnexpectedReturnType

A = TypeVar("A", bound=AttachmentEntry)
B = TypeVar("B", bound="AttachmentEntryRequest")


class AttachmentEntryRequest(BaseAttachmentRequest[AttachmentEntry]):
    """Attachment Entry Request type"""

    @property
    def Invoke(self: B) -> AttachmentEntry:

        _return = super().Invoke

        if type(_return) is not self.generic_type:
            raise UnexpectedReturnType(type(_return), self.generic_type)

        return _return
