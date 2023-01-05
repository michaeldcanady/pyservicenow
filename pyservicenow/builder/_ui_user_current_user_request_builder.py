from __future__ import annotations
from typing import TYPE_CHECKING, Iterable, Optional, Union

if TYPE_CHECKING:
    from pyservicenow.core import ServiceNowClient
from pyrestsdk.requestbuilder import EntityRequestBuilder

# internal imports
from pyservicenow.request._ui_user_current_user_request import UIUserCurrentUserRequest
from pyservicenow.types.models import ServiceNowHeaderOption, ServiceNowQueryOption


class UIUserCurrentUserRequestBuilder(EntityRequestBuilder):
    def __init__(self, request_url: str, client: ServiceNowClient) -> None:
        super().__init__(request_url, client)

    @property
    def request(self) -> UIUserCurrentUserRequest:
        return self.Request(None)

    def Request(
        self,
        options: Optional[
            Iterable[Union[ServiceNowQueryOption, ServiceNowHeaderOption]]
        ],
    ) -> UIUserCurrentUserRequest:
        return UIUserCurrentUserRequest(self.RequestUrl, self.Client, options)
