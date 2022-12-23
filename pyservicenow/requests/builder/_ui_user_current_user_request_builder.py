from ._entity_request_builder import EntityRequestBuilder
from ..request._ui_user_current_user_request import UIUserCurrentUserRequest


class UIUserCurrentUserRequestBuilder(EntityRequestBuilder):

    def __init__(self, request_url: str, client) -> None:
        super().__init__(request_url, client)

    @property
    def Request(self) -> UIUserCurrentUserRequest:
        return UIUserCurrentUserRequest(self.RequestUrl, self.Client, None)