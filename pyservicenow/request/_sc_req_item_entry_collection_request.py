"""Houses SC Req Item Entry Collection Request"""

from __future__ import annotations
from typing import TypeVar, final

from pyservicenow.request.request_extensions import SupportsSysparamQuery
from pyservicenow.request._table_entry_collection_request import TableEntryCollectionRequest
from pyservicenow.types.models import RequestedItem

S = TypeVar("S", bound=RequestedItem)


@final
class SCReqItemEntryCollectionRequest(TableEntryCollectionRequest[RequestedItem], SupportsSysparamQuery):
    """SC Req Item Entry Collection Request Type"""
