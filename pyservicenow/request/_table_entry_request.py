"""Houses table entry request"""

from __future__ import annotations
from typing import TypeVar

from pyrestsdk.request.supports_types import SupportsInvokeRequest

from pyservicenow.request._base_table_request import BaseTableRequest
from pyservicenow.types.models import ServiceNowEntry
from pyservicenow.types.exceptions import UnexpectedReturnType

S = TypeVar("S", bound=ServiceNowEntry)


class TableEntryRequest(BaseTableRequest[S], SupportsInvokeRequest):
    """The base Table Entry Request"""