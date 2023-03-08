
from pyrestsdk.request.supports_types import SupportsInvokeRequest

from pyservicenow.request._base_servicenow_request import BaseServiceNowEntryRequest

from pyservicenow.types.models import KnowledgeArticleEntry

class KnowledgeArticleEntryRequest(SupportsInvokeRequest, BaseServiceNowEntryRequest[KnowledgeArticleEntry]):
    pass