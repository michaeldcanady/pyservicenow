"""houses UI User Current User Request Builder"""

from typing import Iterable, Optional, Union

from pyrestsdk.requestbuilder import EntityRequestBuilder

from pyservicenow.request import UIUserCurrentUserRequest
from pyservicenow.types.models import ServiceNowHeaderOption, ServiceNowQueryOption


class UIUserCurrentUserRequestBuilder(EntityRequestBuilder[UIUserCurrentUserRequest]):
    """The UI User Current User Request Builder type"""

    def request_with_options(
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

        return UIUserCurrentUserRequest(self.request_url, self.request_client, options)
