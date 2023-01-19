"""Houses base attachment request"""

from __future__ import annotations
from typing import TypeVar

# Interal Imports
from pyservicenow.request._base_servicenow_request import BaseServiceNowEntryRequest
from pyservicenow.request.request_extensions import (
    SupportsSysparamOffset,
    SupportsSysparamLimit,
    SupportsSysparamQuery,
)
from pyservicenow.types.models import AttachmentEntry

A = TypeVar("A", bound=AttachmentEntry)


class BaseAttachmentRequest(
    BaseServiceNowEntryRequest[A],
    SupportsSysparamOffset,
    SupportsSysparamLimit,
    SupportsSysparamQuery,
):
    """Base Attachment Request type"""
