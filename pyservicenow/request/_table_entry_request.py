"""Houses table entry request"""

from __future__ import annotations
from typing import TypeVar
from pyservicenow.request._base_table_request import BaseTableRequest
from pyservicenow.types.models import ServiceNowEntry
from pyservicenow.types.exceptions import UnexpectedReturnType

S = TypeVar("S", bound=ServiceNowEntry)
B = TypeVar("B", bound="TableEntryRequest")


class TableEntryRequest(BaseTableRequest[S]):
    """The base Table Entry Request"""

    @property
    def Invoke(self: B) -> S:
        """Invokes the specified method"""

        _return = super().Invoke

        if isinstance(_return, list) or _return is None:
            raise UnexpectedReturnType(type(_return), self.GenericType)

        return _return
