from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from pyservicenow.core import ServiceNowClient

from pyrestsdk.requestbuilder import EntityRequestBuilder
# internal imports
from pyservicenow.builder._ui_user_request_builder import UIUserRequestBuilder


class UIRequestBuilder(EntityRequestBuilder):

    def __init__(self, request_url: str, client: ServiceNowClient) -> None:
        super().__init__(request_url, client)

    @property
    def User(self) -> UIUserRequestBuilder:

        return UIUserRequestBuilder(self.AppendSegmentToRequestUrl("user"), self.Client)
