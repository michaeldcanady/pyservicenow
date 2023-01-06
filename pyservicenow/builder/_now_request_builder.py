"""Houses the Now Request Builder"""

from __future__ import annotations
from typing import TYPE_CHECKING
from pyrestsdk.requestbuilder import EntityRequestBuilder, BaseRequestBuilder
from pyservicenow.builder._table_request_builder import TableRequestBuilder
from pyservicenow.builder._ui_request_builder import UIRequestBuilder
from pyservicenow.builder._attachment_request_builder import AttachmentRequestBuilder

if TYPE_CHECKING:
    from pyservicenow.core import ServiceNowClient


class NowRequestBuilder(BaseRequestBuilder):
    """The Now Request Builder type"""

    def Table(self, table_name: str) -> TableRequestBuilder:
        """Get a specified serviceNow table

        Args:
            table_name (str): table name

        Returns:
            TableRequestBuilder: The table path
        """

        return TableRequestBuilder(
            self.append_segment_to_request_url(f"/table/{table_name}"), self.Client
        )

    @property
    def Attachment(self) -> AttachmentRequestBuilder:
        """Gets attachment request builder

        Returns:
            AttachmentRequestBuilder: attachment request builder
        """

        return AttachmentRequestBuilder(
            self.append_segment_to_request_url("attachment"), self.Client
        )

    @property
    def UI(self) -> UIRequestBuilder:
        """Gets UI request builder

        Returns:
            UIRequestBuilder: UI request builder
        """

        return UIRequestBuilder(self.append_segment_to_request_url("ui"), self.Client)
