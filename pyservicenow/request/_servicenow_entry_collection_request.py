"""Houses ServiceNow Table Entry Collection Request Type"""

from pyservicenow.request._table_entry_collection_request import (
    TableEntryCollectionRequest,
)

from pyservicenow.types.models import ServiceNowEntry


class ServiceNowTableEntryCollectionRequest(
    TableEntryCollectionRequest[ServiceNowEntry]
):
    """ServiceNow Table Entry Collection Request Type"""

    pass
