"""Houses the UI User Current User Request"""

from pyrestsdk.request.supports_types import SupportsInvokeRequest

from pyservicenow.request._base_servicenow_request import BaseServiceNowEntryRequest
from pyservicenow.types.models import CurrentUser

class UIUserCurrentUserRequest(BaseServiceNowEntryRequest[CurrentUser], SupportsInvokeRequest):
    """The Table Entry Collection Request"""
