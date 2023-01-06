"""Houses UI User Request Builder"""

from __future__ import annotations
from typing import TYPE_CHECKING
from pyrestsdk.requestbuilder import BaseRequestBuilder
from pyservicenow.builder._ui_user_current_user_request_builder import (
    UIUserCurrentUserRequestBuilder,
)

if TYPE_CHECKING:
    from pyservicenow.core import ServiceNowClient


class UIUserRequestBuilder(BaseRequestBuilder):
    """The UI User Request Builder type"""

    @property
    def CurrentUser(self) -> UIUserCurrentUserRequestBuilder:
        """Gets a UI User Current User Request Builder

        Returns:
            UIUserCurrentUserRequestBuilder: UI User Current User Request Builder
        """

        return UIUserCurrentUserRequestBuilder(
            self.AppendSegmentToRequestUrl("current_user"), self.Client
        )
