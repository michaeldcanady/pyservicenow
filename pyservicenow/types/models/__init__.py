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

from pyservicenow.types.models._knowledge_article_entry import KnowledgeArticleEntry

from pyservicenow.types.models._abstract_attachment_entry import AbstractAttachmentEntry
from pyservicenow.types.models._abstract_current_user import AbstractCurrentUser
from pyservicenow.types.models._abstract_servicenow_entry import AbstractServiceNowEntry
from pyservicenow.types.models._abstract_servicenow_property import AbstractServiceNowProperty
from pyservicenow.types.models._abstract_servicenow_propery_collection import (
    AbstractServiceNowPropertyCollection,
)

if version_info < (3, 10):
    from pyservicenow.types.models._query_builder39 import QueryBuilder
else:
    from pyservicenow.types.models._query_builder310 import QueryBuilder

__all__ = [
    "AbstractAttachmentEntry",
    "AbstractCurrentUser",
    "AbstractServiceNowProperty",
    "AbstractServiceNowEntry",
    "AbstractServiceNowPropertyCollection",
    "AttachmentEntry",
    "QueryBuilder",
    "ServiceNowPropertyCollection",
    "ServiceNowEntry",
    "CurrentUser",
    "KnowledgeArticleEntry",
    "ServiceNowQueryOption",
    "ServiceNowHeaderOption",
]
