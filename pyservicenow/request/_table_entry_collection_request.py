from __future__ import annotations
import typing
from typing import TypeVar, Type, List, Optional, Generic, TYPE_CHECKING, Iterable, Union

if TYPE_CHECKING:
    from pyservicenow.core import ServiceNowClient

# Interal Imports
from pyservicenow.types.models import ServiceNowEntry, ServiceNowQueryOption, ServiceNowHeaderOption
from pyservicenow.request._base_table_request import BaseTableRequest

S = TypeVar("S", bound=ServiceNowEntry)


class TableEntryCollectionRequest(BaseTableRequest):
    """The Table Entry Collection Request"""

    def __init__(self, _return_type: Type[S], request_url: str, client: 'ServiceNowClient', options: Iterable[Union[ServiceNowQueryOption, ServiceNowHeaderOption]]) -> None:
        super().__init__(_return_type, request_url, client, options)