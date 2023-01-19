"""Houses Attachment Entry Collection Request"""

from __future__ import annotations
from typing import TypeVar

from pyrestsdk.request.supports_types import SupportsInvokeCollectionRequest

from pyservicenow.request._base_attachment_request import BaseAttachmentRequest
from pyservicenow.types.models import AttachmentEntry

T = TypeVar("T", bound="BaseAttachmentRequest")
A = TypeVar("A", bound=AttachmentEntry)
B = TypeVar("B", bound="AttachmentEntryCollectionRequest")


class AttachmentEntryCollectionRequest(BaseAttachmentRequest[AttachmentEntry], SupportsInvokeCollectionRequest):
    """Attachment Entry Collection Request type"""
