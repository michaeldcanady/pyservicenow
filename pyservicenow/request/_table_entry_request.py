"""Houses table entry request"""

from __future__ import annotations
from typing import TypeVar
from pyrestsdk.request.supports_types import SupportsInvokeRequest
from pyservicenow.request._base_table_request import BaseTableRequest
from pyservicenow.types.models import ServiceNowEntry
from pyservicenow.types.exceptions import UnexpectedReturnType

S = TypeVar("S", bound=ServiceNowEntry)


class TableEntryRequest(BaseTableRequest[S], SupportsInvokeRequest):
    """The base Table Entry Request"""

    @property
    def invoke_request(self) -> S:
        """Invokes the specified method"""

        _return = super().Send(self.input_object)

        if not isinstance(_return, self.generic_type) or _return is None:
            raise UnexpectedReturnType(type(_return), self.generic_type)

        return _return
