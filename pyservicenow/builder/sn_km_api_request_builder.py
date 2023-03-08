"""Houses the ServiceNow Knowledge Management API Request Builder"""

from typing import TypeVar

from pyrestsdk.requestbuilder import BaseRequestBuilder

from pyservicenow.builder.knowledge_request_builder import KnowledgeRequestBuilder

N = TypeVar("N", bound="SnKmAPIRequestBuilder")


class SnKmAPIRequestBuilder(BaseRequestBuilder):
    #https://developer.servicenow.com/dev.do#!/reference/api/tokyo/rest/knowledge-management-api
    
    @property
    def knowledge(self: N) -> KnowledgeRequestBuilder:
        
        return KnowledgeRequestBuilder(self.append_segment_to_request_url("knowledge"), self.request_client)