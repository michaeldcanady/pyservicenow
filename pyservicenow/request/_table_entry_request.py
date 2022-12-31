from __future__ import annotations
from typing import TypeVar, Type, TYPE_CHECKING, Iterable, Union, Optional
if TYPE_CHECKING:
    from pyservicenow.core import ServiceNowClient

# Interal Imports
from pyservicenow.request._base_table_request import BaseTableRequest
from pyservicenow.types.models import (
    ServiceNowEntry,
    ServiceNowHeaderOption,
    ServiceNowQueryOption,
)

S = TypeVar("S", bound=ServiceNowEntry)
B = TypeVar("B", bound="TableEntryRequest")


class TableEntryRequest(BaseTableRequest):
    """The base Table Entry Request"""

    def __init__(
        self,
        _return_type: Type[S],
        request_url: str,
        client: "ServiceNowClient",
        options: Optional[
            Iterable[Union[ServiceNowQueryOption, ServiceNowHeaderOption]]
        ],
    ) -> None:
        super().__init__(_return_type, request_url, client, options)
