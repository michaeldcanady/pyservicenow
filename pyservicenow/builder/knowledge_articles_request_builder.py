"""Houses the Knowledge Articles Request Builder"""

from typing import TypeVar, Optional, Iterable

from pyrestsdk.type.model import Option

from pyrestsdk.requestbuilder import EntityRequestBuilder

from pyservicenow.request import KnowledgeArticleEntryCollectionRequest, KnowledgeArticleEntryRequest

N = TypeVar("N", bound="KnowledgeArticlesRequestBuilder")

O = TypeVar("O", bound=Option)


class KnowledgeArticlesRequestBuilder(EntityRequestBuilder):
    
    @property
    def request(self) -> KnowledgeArticleEntryCollectionRequest:
        return self.request_with_options(None)
    
    def request_with_options(self, options: Optional[Iterable[O]]) -> KnowledgeArticleEntryCollectionRequest:
        
        return KnowledgeArticleEntryCollectionRequest(self.request_url, self.request_client, options)
    
    def id(self, id: str) -> KnowledgeArticleEntryRequest:
        
        return KnowledgeArticleEntryRequest(self.append_segment_to_request_url(id), self.request_client, None)