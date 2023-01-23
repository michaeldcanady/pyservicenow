"""Houses the Table Entry Collection Request"""

from __future__ import annotations
from typing import TypeVar, List, Type

from pyrestsdk.request.supports_types import SupportsInvokeCollectionRequest

from pyservicenow.types.models import ServiceNowEntry
from pyservicenow.types.exceptions import UnexpectedReturnType
from pyservicenow.request._base_table_request import BaseTableRequest

S = TypeVar("S", bound=ServiceNowEntry)


class TableEntryCollectionRequest(SupportsInvokeCollectionRequest, BaseTableRequest[S]):
    """The Table Entry Collection Request"""
