from ._entity_request_builder import EntityRequestBuilder
from ._ui_user_current_user_request_builder import UIUserCurrentUserRequestBuilder

class UIUserRequestBuilder(EntityRequestBuilder):

    def __init__(self, request_url: str, client) -> None:
        super().__init__(request_url, client)

    @property
    def CurrentUser(self) -> UIUserCurrentUserRequestBuilder:

        return UIUserCurrentUserRequestBuilder(self.AppendSegmentToRequestUrl("current_user"), self.Client)