"""Houses the Knowledge Request Builder"""

from typing import TypeVar

from pyrestsdk.requestbuilder import BaseRequestBuilder

from pyservicenow.builder.knowledge_articles_request_builder import KnowledgeArticlesRequestBuilder

N = TypeVar("N", bound="KnowledgeRequestBuilder")


class KnowledgeRequestBuilder(BaseRequestBuilder):
    
    @property
    def articles(self: N) -> KnowledgeArticlesRequestBuilder:
        
        return KnowledgeArticlesRequestBuilder(self.append_segment_to_request_url("articles"), self.request_client)