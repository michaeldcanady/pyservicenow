from ._entity_request_builder import EntityRequestBuilder
from ._table_request_builder import TableRequestBuilder
from ._ui_request_builder import UIRequestBuilder

class NowRequestBuilder(EntityRequestBuilder):

    def __init__(self, request_url: str, client) -> None:
        super().__init__(request_url, client)

    def Table(self, table_name: str) -> TableRequestBuilder:
        """Get a specific serviceNow table

        Args:
            table_name (str): table name

        Returns:
            TableRequestBuilder: The table path
        """

        return TableRequestBuilder(self.AppendSegmentToRequestUrl(f"/table/{table_name}"), self.Client)
    
    @property
    def UI(self) -> UIRequestBuilder:

        return UIRequestBuilder(self.AppendSegmentToRequestUrl("ui"), self.Client)