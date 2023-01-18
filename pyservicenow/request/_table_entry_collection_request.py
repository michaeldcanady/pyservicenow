from __future__ import annotations
from typing import TypeVar, TYPE_CHECKING, Iterable, Union, Optional, List, Type

if TYPE_CHECKING:
    from pyservicenow.core import ServiceNowClient

# Interal Imports
from pyservicenow.types.models import (
    ServiceNowEntry,
    ServiceNowQueryOption,
    ServiceNowHeaderOption,
)
from pyservicenow.types.exceptions import UnexpectedReturnType
from pyservicenow.request._base_table_request import BaseTableRequest

S = TypeVar("S", bound=ServiceNowEntry)
B = TypeVar("B", bound="TableEntryCollectionRequest")


class TableEntryCollectionRequest(BaseTableRequest[S]):
    """The Table Entry Collection Request"""

    def __init__(
        self: B,
        request_url: str,
        client: "ServiceNowClient",
        options: Optional[
            Iterable[Union[ServiceNowQueryOption, ServiceNowHeaderOption]]
        ],
    ) -> None:
        super().__init__(request_url, client, options)

    @property
    def Invoke(self: B) -> List[S]:

        _return = super().Invoke

        _type = self.generic_type

        if type(_return) is not list:
            raise UnexpectedReturnType(type(_return), List[Type[_type]])

        return _return
