"""Houses table entry request"""

from __future__ import annotations
from typing import TypeVar

from pyrestsdk.request.supports_types import SupportsInvokeRequest

from pyservicenow.request._base_table_request import BaseTableRequest
from pyservicenow.types.models import ServiceNowEntry

S = TypeVar("S", bound=ServiceNowEntry)


class TableEntryRequest(SupportsInvokeRequest, BaseTableRequest[S]):
    """The base Table Entry Request"""