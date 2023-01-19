"""Houses UI User Request Builder"""

from pyrestsdk.requestbuilder import BaseRequestBuilder
from pyservicenow.builder._ui_user_current_user_request_builder import (
    UIUserCurrentUserRequestBuilder,
)


class UIUserRequestBuilder(BaseRequestBuilder):
    """The UI User Request Builder type"""

    @property
    def current_user(self) -> UIUserCurrentUserRequestBuilder:
        """Gets a UI User Current User Request Builder

        Returns:
            UIUserCurrentUserRequestBuilder: UI User Current User Request Builder
        """

        return UIUserCurrentUserRequestBuilder(
            self.append_segment_to_request_url("current_user"), self.Client
        )
