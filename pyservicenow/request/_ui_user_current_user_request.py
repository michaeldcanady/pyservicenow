"""Houses the UI User Current User Request"""

from pyrestsdk.request.supports_types import SupportsInvokeRequest
from pyservicenow.request._base_servicenow_request import BaseServiceNowEntryRequest
from pyservicenow.types.models import CurrentUser
from pyservicenow.types.exceptions import UnexpectedReturnType


class UIUserCurrentUserRequest(BaseServiceNowEntryRequest[CurrentUser], SupportsInvokeRequest):
    """The Table Entry Collection Request"""

    @property
    def invoke_request(self) -> CurrentUser:
        """Invokes the specified method"""

        _return = super().Send(self.input_object)

        if not isinstance(_return, self.generic_type) or _return is None:
            raise UnexpectedReturnType(type(_return), type(self.generic_type))

        return _return
