"""House Attachment Entry Request"""

from pyrestsdk.request.supports_types import SupportsInvokeRequest
from pyservicenow.types.models import AttachmentEntry
from pyservicenow.request._base_attachment_request import BaseAttachmentRequest
from pyservicenow.types.models import (
    AttachmentEntry,
)


class AttachmentEntryRequest(BaseAttachmentRequest[AttachmentEntry], SupportsInvokeRequest):
    """Attachment Entry Request Type"""
