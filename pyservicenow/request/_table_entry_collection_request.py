"""Houses the Table Entry Collection Request"""

from __future__ import annotations
from typing import TypeVar, List, Type
from pyservicenow.types.models import ServiceNowEntry
from pyservicenow.types.exceptions import UnexpectedReturnType
from pyservicenow.request._base_table_request import BaseTableRequest

S = TypeVar("S", bound=ServiceNowEntry)
B = TypeVar("B", bound="TableEntryCollectionRequest")


class TableEntryCollectionRequest(BaseTableRequest[S]):
    """The Table Entry Collection Request"""

    @property
    def Invoke(self: B) -> List[S]:
        """Invokes the specified method"""
        
        print(self.GenericType)

        _return = super().Invoke

        _type = self.generic_type

        if not isinstance(_return, list):
            raise UnexpectedReturnType(type(_return), List[Type[_type]])

        return _return
