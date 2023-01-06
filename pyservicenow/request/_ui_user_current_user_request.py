"""Houses the UI User Current User Request"""

from __future__ import annotations
from typing import TypeVar
from pyservicenow.request._base_servicenow_request import BaseServiceNowEntryRequest
from pyservicenow.types.models import CurrentUser
from pyservicenow.types.exceptions import UnexpectedReturnType

B = TypeVar("B", bound="UIUserCurrentUserRequest")


class UIUserCurrentUserRequest(BaseServiceNowEntryRequest[CurrentUser]):
    """The Table Entry Collection Request"""

    @property
    def Invoke(self: B) -> CurrentUser:
        """Invokes the specified method"""

        _return = super().Invoke

        if not isinstance(_return, self.GenericType):
            raise UnexpectedReturnType(type(_return), self.GenericType)

        return _return
