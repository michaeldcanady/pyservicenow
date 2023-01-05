from __future__ import annotations
from typing import TypeVar, TYPE_CHECKING, Iterable, Union, Optional

if TYPE_CHECKING:
    from pyservicenow.core import ServiceNowClient

# Interal Imports
from pyservicenow.request._base_table_request import BaseTableRequest
from pyservicenow.types.models import (
    ServiceNowEntry,
    ServiceNowHeaderOption,
    ServiceNowQueryOption,
)
from pyservicenow.types.exceptions import UnexpectedReturnType

S = TypeVar("S", bound=ServiceNowEntry)
B = TypeVar("B", bound="TableEntryRequest")


class TableEntryRequest(BaseTableRequest[S]):
    """The base Table Entry Request"""

    def __init__(
        self,
        request_url: str,
        client: "ServiceNowClient",
        options: Optional[
            Iterable[Union[ServiceNowQueryOption, ServiceNowHeaderOption]]
        ],
    ) -> None:
        super().__init__(request_url, client, options)

    @property
    def Invoke(self: B) -> S:

        _return = super().Invoke

        if type(_return) is not self.GenericType:
            raise UnexpectedReturnType(type(_return), self.GenericType)

        return _return
