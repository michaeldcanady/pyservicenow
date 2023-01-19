"""Houses Attachment Entry Request"""

from __future__ import annotations
from typing import TypeVar

from pyrestsdk.request.supports_types import SupportsInvokeRequest

from pyservicenow.request._base_attachment_request import BaseAttachmentRequest
from pyservicenow.types.models import AttachmentEntry
from pyservicenow.types.exceptions import UnexpectedReturnType

A = TypeVar("A", bound=AttachmentEntry)
B = TypeVar("B", bound="AttachmentEntryRequest")


class AttachmentEntryRequest(BaseAttachmentRequest[AttachmentEntry], SupportsInvokeRequest):
    """Attachment Entry Request type"""
