from typing import Union, TypeVar, Type, List, Optional, Generic

from pyrestsdk.request import BaseRequest
from pyrestsdk.type.enum import HttpsMethod

# Interal Imports
from pyservicenow.types.enums import MimeTypeNames, Header
from pyservicenow.types.models import ServiceNowEntry
from pyservicenow.types.models import ServiceNowHeaderOption
from pyservicenow.types.exceptions import UnexpectedReturnType

T = TypeVar("T", bound=BaseRequest)
S = TypeVar("S", bound=ServiceNowEntry)


class UIUserCurrentUserRequest(BaseRequest):
    """The Table Entry Collection Request"""

    def Get(self) -> "CurrentUser":
        """Gets a single Service-Now Entry

        Returns:
            ServiceNowEntry: The Service-Now Entry
        """

        # MimeTypeNames.Application.JSON
        self._headers.append(
            ServiceNowHeaderOption(Header.Accept, MimeTypeNames.Application.Json)
        )
        self.Method = HttpsMethod.GET

        return self.Send(CurrentUser, None)


from pyservicenow.types.models import CurrentUser
