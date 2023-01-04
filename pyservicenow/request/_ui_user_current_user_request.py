from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Iterable, Union, TypeVar

if TYPE_CHECKING:
    from pyservicenow.core import ServiceNowClient

# Interal Imports
from pyservicenow.request._base_servicenow_request import BaseServiceNowEntryRequest
from pyservicenow.types.models import (
    CurrentUser,
    ServiceNowHeaderOption,
    ServiceNowQueryOption,
)
from pyservicenow.types.exceptions import UnexpectedReturnType

B = TypeVar("B", bound="UIUserCurrentUserRequest")


class UIUserCurrentUserRequest(BaseServiceNowEntryRequest[CurrentUser]):
    """The Table Entry Collection Request"""

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
    def Invoke(self: B) -> CurrentUser:

        _return = super().Invoke

        if type(_return) is not self.GenericType:
            raise UnexpectedReturnType(type(_return), self.GenericType)

        return _return
