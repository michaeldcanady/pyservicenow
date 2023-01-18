from __future__ import annotations
from typing import TYPE_CHECKING
from pyrestsdk.requestbuilder import EntityRequestBuilder
from pyservicenow.builder._ui_user_request_builder import UIUserRequestBuilder

if TYPE_CHECKING:
    from pyservicenow.core import ServiceNowClient


class UIRequestBuilder(EntityRequestBuilder):
    """The UI Request Builder type"""

    @property
    def User(self) -> UIUserRequestBuilder:
        """Constructs a UI User request builder

        Returns:
            UIUserRequestBuilder: UI User request builder
        """

        return UIUserRequestBuilder(self.append_segment_to_request_url("user"), self.Client)
