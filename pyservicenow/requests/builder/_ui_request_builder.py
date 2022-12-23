from ._entity_request_builder import EntityRequestBuilder
from ._ui_user_request_builder import UIUserRequestBuilder


class UIRequestBuilder(EntityRequestBuilder):

    def __init__(self, request_url: str, client) -> None:
        super().__init__(request_url, client)

    @property
    def User(self) -> UIUserRequestBuilder:

        return UIUserRequestBuilder(self.AppendSegmentToRequestUrl("user"), self.Client)
