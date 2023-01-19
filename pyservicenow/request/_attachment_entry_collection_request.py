"""Houses Attachment Entry Collection Request"""

from __future__ import annotations
from typing import TypeVar, List
from pyservicenow.request._base_attachment_request import BaseAttachmentRequest
from pyservicenow.types.models import AttachmentEntry
from pyservicenow.types.exceptions import UnexpectedReturnType

T = TypeVar("T", bound="BaseAttachmentRequest")
A = TypeVar("A", bound=AttachmentEntry)
B = TypeVar("B", bound="AttachmentEntryCollectionRequest")


class AttachmentEntryCollectionRequest(BaseAttachmentRequest[AttachmentEntry]):
    """Attachment Entry Collection Request type"""

    @property
    def Invoke(self: B) -> List[AttachmentEntry]:
        """Invokes the specified method"""

        _return = super().Invoke

        if not isinstance(_return, list) or _return is None:
            raise UnexpectedReturnType(type(_return), List[AttachmentEntry])

        return _return
