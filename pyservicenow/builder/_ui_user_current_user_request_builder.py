from __future__ import annotations
from typing import TYPE_CHECKING, Iterable, Optional, Union
from pyrestsdk.requestbuilder import EntityRequestBuilder
from pyservicenow.request._ui_user_current_user_request import UIUserCurrentUserRequest
from pyservicenow.types.models import ServiceNowHeaderOption, ServiceNowQueryOption

if TYPE_CHECKING:
    from pyservicenow.core import ServiceNowClient

class UIUserCurrentUserRequestBuilder(EntityRequestBuilder):
    """The UI User Current User Request Builder type"""

    @property
    def request(self) -> UIUserCurrentUserRequest:
        """Constructs a UI User CurrentUser Request

        Returns:
            UIUserCurrentUserRequest: The constructed UI User CurrentUser Request
        """
        
        return self.Request(None)

    def Request(
        self,
        options: Optional[
            Iterable[Union[ServiceNowQueryOption, ServiceNowHeaderOption]]
        ],
    ) -> UIUserCurrentUserRequest:
        """Constructs a UI User CurrentUser Request

        Args:
            options (Optional[ Iterable[Union[ServiceNowQueryOption, ServiceNowHeaderOption]] ]): query or header options to include in the request

        Returns:
            UIUserCurrentUserRequest: The constructed UI User CurrentUser Request
        """
        
        return UIUserCurrentUserRequest(self.RequestUrl, self.Client, options)
