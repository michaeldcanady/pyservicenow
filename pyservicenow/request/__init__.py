"""Houses all requests"""

from pyservicenow.request._attachment_entry_collection_request import (
    AttachmentEntryCollectionRequest,
)

from pyservicenow.request._attachment_file_entry_request import (
    AttachmentFileEntryRequest
)

from pyservicenow.request._attachment_entry_request import AttachmentEntryRequest
from pyservicenow.request._base_attachment_request import BaseAttachmentRequest
from pyservicenow.request._base_servicenow_request import BaseServiceNowEntryRequest
from pyservicenow.request._base_table_request import BaseTableRequest
from pyservicenow.request._servicenow_entry_collection_request import (
    ServiceNowTableEntryCollectionRequest,
)
from pyservicenow.request._table_entry_collection_request import (
    TableEntryCollectionRequest,
)

from pyservicenow.request._knowledge_article_entry_collection_request import KnowledgeArticleEntryCollectionRequest
from pyservicenow.request._knowledge_article_entry_request import KnowledgeArticleEntryRequest

from pyservicenow.request._table_entry_request import TableEntryRequest
from pyservicenow.request._ui_user_current_user_request import UIUserCurrentUserRequest

__all__ = [
    "AttachmentFileEntryRequest",
    "AttachmentEntryCollectionRequest",
    "AttachmentEntryRequest",
    "BaseAttachmentRequest",
    "BaseServiceNowEntryRequest",
    "BaseTableRequest",
    "KnowledgeArticleEntryCollectionRequest",
    "KnowledgeArticleEntryRequest",
    "ServiceNowTableEntryCollectionRequest",
    "TableEntryCollectionRequest",
    "TableEntryRequest",
    "UIUserCurrentUserRequest",
]
