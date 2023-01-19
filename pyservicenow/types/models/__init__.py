"""Houses All avaliable Models"""

from sys import version_info

from pyservicenow.types.models._servicenow_property_collection import (
    ServiceNowPropertyCollection,
)
from pyservicenow.types.models._servicenow_entry import ServiceNowEntry
from pyservicenow.types.models._current_user import CurrentUser
from pyservicenow.types.models._servicenow_query_options import ServiceNowQueryOption
from pyservicenow.types.models._servicenow_header_option import ServiceNowHeaderOption
from pyservicenow.types.models._attachment_entry import AttachmentEntry

if version_info < (3,10):
    from pyservicenow.types.models._query_builder39 import QueryBuilder
else:
    from pyservicenow.types.models._query_builder310 import QueryBuilder

__all__ = [
    "AttachmentEntry",
    "QueryBuilder",
    "ServiceNowPropertyCollection",
    "ServiceNowEntry",
    "CurrentUser",
    "ServiceNowQueryOption",
    "ServiceNowHeaderOption",
]
