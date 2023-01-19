"""Houses all requests"""

from pyservicenow.request._table_entry_request import TableEntryRequest
from pyservicenow.request._attachment_entry_collection_request import (
    AttachmentEntryCollectionRequest,
)
from pyservicenow.request._attachment_entry_request import AttachmentEntryRequest

__all__ = [
    "TableEntryRequest",
    "AttachmentEntryRequest",
    "AttachmentEntryCollectionRequest",
]
