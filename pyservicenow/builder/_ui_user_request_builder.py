from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from pyservicenow.core import ServiceNowClient
from pyrestsdk.requestbuilder import EntityRequestBuilder

# internal imports
from pyservicenow.builder._ui_user_current_user_request_builder import UIUserCurrentUserRequestBuilder

class UIUserRequestBuilder(EntityRequestBuilder):

    def __init__(self, request_url: str, client: ServiceNowClient) -> None:
        super().__init__(request_url, client)

    @property
    def CurrentUser(self) -> UIUserCurrentUserRequestBuilder:

        return UIUserCurrentUserRequestBuilder(self.AppendSegmentToRequestUrl("current_user"), self.Client)