"""Houses the Now Request Builder"""

from typing import TypeVar

from pyrestsdk.requestbuilder import BaseRequestBuilder

from pyservicenow.builder._table_request_builder import TableRequestBuilder
from pyservicenow.builder._ui_request_builder import UIRequestBuilder
from pyservicenow.builder._attachment_request_builder import AttachmentRequestBuilder

N = TypeVar("N", bound="NowRequestBuilder")

class NowRequestBuilder(BaseRequestBuilder):
    """The Now Request Builder type"""

    def table_api(self:N, table_name: str) -> TableRequestBuilder:
        """Get a specified serviceNow table

        Args:
            table_name (str): table name

        Returns:
            TableRequestBuilder: The table path
        """

        return TableRequestBuilder(
            self.append_segment_to_request_url(f"/table/{table_name}"), self.request_client
        )
        
    @property
    def v2(self:N) -> N:
        
        self.append_segment_to_request_url("/v2")
        
        return self
    
    @property
    def v1(self:N) -> N:
        
        self.append_segment_to_request_url("/v1")
        
        return self

    @property
    def attachment_api(self) -> AttachmentRequestBuilder:
        """Gets attachment request builder

        Returns:
            AttachmentRequestBuilder: attachment request builder
        """

        return AttachmentRequestBuilder(
            self.append_segment_to_request_url("attachment"), self.request_client
        )

    @property
    def ui_api(self) -> UIRequestBuilder:
        """Gets UI request builder

        Returns:
            UIRequestBuilder: UI request builder
        """

        return UIRequestBuilder(self.append_segment_to_request_url("ui"), self.request_client)
