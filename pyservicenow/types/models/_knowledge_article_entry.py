"""Houses attachment Entry Model"""

from __future__ import annotations

from typing import List

from pyservicenow.types.models._servicenow_entry import ServiceNowEntry


class KnowledgeArticleEntry(ServiceNowEntry):
    
    def __init__(self, client) -> None:
        super().__init__(client)
        
    def content(self) -> str:
        
        return self.get("content", str)
    
    def template(self) -> bool:
        
        return self.get("template", bool)
    
    def number(self) -> str:
        
        return self.get("number", str)
    
    def short_description(self) -> str:
        
        return self.get("short_description", str)
    
    def display_attachments(self) -> bool:
        
        return self.get("display_attachments", bool)
    
    def attachments(self) -> List:
        
        return self.get("attachments", list)
    
    def embedded_content(self) -> List:
        
        return self.get("embedded_content", list)