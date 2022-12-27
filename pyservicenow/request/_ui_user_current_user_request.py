from typing import Union, TypeVar, Type, List, Optional, Generic

from pyrestsdk.request import BaseRequest

# Interal Imports
from pyservicenow.types.enums import HttpsMethods
from pyservicenow.types.models import ServiceNowEntry
from pyservicenow.types.exceptions import UnexpectedReturnType

T = TypeVar("T", bound=BaseRequest)
S = TypeVar("S", bound=ServiceNowEntry)


class UIUserCurrentUserRequest(BaseRequest):
    """The Table Entry Collection Request
    """

    def Get(self) -> 'CurrentUser':
        """Gets a single Service-Now Entry

        Returns:
            ServiceNowEntry: The Service-Now Entry
        """


        # MimeTypeNames.Application.JSON
        self._headers["Accept"] = "application/json"
        self.Method = HttpsMethods.GET

        return self.Send(CurrentUser, None)

from pyservicenow.types.models import CurrentUser