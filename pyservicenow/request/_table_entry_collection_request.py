"""Houses the Table Entry Collection Request"""

from __future__ import annotations
from typing import TypeVar, List, Type
from pyrestsdk.request.supports_types import SupportsInvokeRequest
from pyservicenow.types.models import ServiceNowEntry
from pyservicenow.types.exceptions import UnexpectedReturnType
from pyservicenow.request._base_table_request import BaseTableRequest

S = TypeVar("S", bound=ServiceNowEntry)


class TableEntryCollectionRequest(BaseTableRequest[S], SupportsInvokeRequest):
    """The Table Entry Collection Request"""

    @property
    def Invoke(self) -> List[S]:
        """Invokes the specified method"""

        _return = super().Send(self.input_object)

        _type = self.generic_type

        if not isinstance(_return, list) or _return is None:
            raise UnexpectedReturnType(type(_return), List[Type[_type]])

        return _return
