"""Houses the Table Entry Collection Request"""

from __future__ import annotations
from typing import TypeVar

from pyrestsdk.request.supports_types import SupportsInvokeCollectionRequest, SupportsPostMethod

from pyservicenow.types.models import ServiceNowEntry
from pyservicenow.request._base_table_request import BaseTableRequest

S = TypeVar("S", bound=ServiceNowEntry)


class TableEntryCollectionRequest(BaseTableRequest[S], SupportsInvokeCollectionRequest, SupportsPostMethod):
    """The Table Entry Collection Request"""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
