"""Houses SC Req Item Request Builder"""

from __future__ import annotations
from typing import Iterable, Optional, Union

from pyservicenow.types.models import ServiceNowQueryOption, ServiceNowHeaderOption
from pyservicenow.builder._table_request_builder import TableRequestBuilder
from pyservicenow.request import SCReqItemEntryCollectionRequest


class SCReqItemRequestBuilder(TableRequestBuilder):
    """SC Req Item Request Builder Type"""

    @property
    def request(self) -> SCReqItemEntryCollectionRequest:
        """Builds a SCReqItemEntryCollectionRequest without options"""

        return self.request_with_options(None)

    def request_with_options(self, options: Optional[Iterable[Union[ServiceNowQueryOption, ServiceNowHeaderOption]]]) -> SCReqItemEntryCollectionRequest:
        """Builds a SCReqItemEntryCollectionRequest with options"""

        return SCReqItemEntryCollectionRequest(self.request_url, self.request_client, options)

    def request_by_id(self, sys_id: str) -> None:
        """Gets the SCReqItem entry request

        Args:
            sys_id (str): The sys id of the entry

        Returns:
            SCRequestEntryRequest: The SCReqItem entry request
        """

        raise NotImplementedError("request_by_id is not implemented")
