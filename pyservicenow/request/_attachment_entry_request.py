"""House Attachment Entry Request"""

from pyrestsdk.request.supports_types import SupportsInvokeRequest, SupportsPutMethod, SupportsDeleteMethod
from pyservicenow.types.models import AttachmentEntry
from pyservicenow.request._base_attachment_request import BaseAttachmentRequest
from pyservicenow.types.models import (
    AttachmentEntry,
)


class AttachmentEntryRequest(
    SupportsInvokeRequest,
    SupportsPutMethod,
    SupportsDeleteMethod,
    BaseAttachmentRequest[AttachmentEntry],
):
    """Attachment Entry Request Type"""
