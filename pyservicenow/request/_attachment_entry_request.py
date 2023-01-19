"""House Attachment Entry Request"""

from typing import TypeVar

from pyservicenow.types.models import AttachmentEntry
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
    """Attachment Entry Request Type"""

    @property
    def Invoke(self: B) -> AttachmentEntry:

        _return = super().Invoke

        if not isinstance(_return, self.generic_type) or _return is None:
            raise UnexpectedReturnType(type(_return), self.generic_type)

        return _return
