"""houses UI User Current User Request Builder"""

from typing import Iterable, Optional, Union
from pyrestsdk.requestbuilder import EntityRequestBuilder
from pyservicenow.request._ui_user_current_user_request import UIUserCurrentUserRequest
from pyservicenow.types.models import ServiceNowHeaderOption, ServiceNowQueryOption


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
            options (Optional[ Iterable[Union[ServiceNowQueryOption, ServiceNowHeaderOption]] ]):
            query or header options to include in the request

        Returns:
            UIUserCurrentUserRequest: The constructed UI User CurrentUser Request
        """

        return UIUserCurrentUserRequest(self.request_url, self.Client, options)
