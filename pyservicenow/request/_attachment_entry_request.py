"""House Attachment Entry Request"""

from pyrestsdk.request.supports_types import SupportsInvokeRequest
from pyservicenow.types.models import AttachmentEntry
from pyservicenow.request._base_attachment_request import BaseAttachmentRequest
from pyservicenow.types.models import (
    AttachmentEntry,
)
from pyservicenow.types.exceptions import UnexpectedReturnType


class AttachmentEntryRequest(BaseAttachmentRequest[AttachmentEntry], SupportsInvokeRequest):
    """Attachment Entry Request Type"""

    @property
    def invoke_request(self) -> AttachmentEntry:

        _return = super().Send(self.input_object)

        if not isinstance(_return, self.generic_type) or _return is None:
            raise UnexpectedReturnType(type(_return), self.generic_type)

        return _return
