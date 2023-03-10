from pyrestsdk.request.supports_types import (
    SupportsInvokeRequest,
    SupportsPostMethod
)

from pyrestsdk.type.enum import HttpsMethod

from pyservicenow.request._base_servicenow_request import BaseServiceNowEntryRequest

from pyservicenow.types.models import ServiceNowQueryOption

from pyservicenow.types.models import (
    AttachmentEntry,
)

class AttachmentFileEntryRequest(SupportsInvokeRequest, SupportsPostMethod, BaseServiceNowEntryRequest[AttachmentEntry]):
    """Attachement File Entry Request Type"""
    
    
    def Post(self, file_path: str):
        
        input_object = None
        
        with open(file_path) as file:
            input_object = file.read()
        
        self._update_request_type(HttpsMethod.POST, input_object)
        
        return self
    
    def table_name(self, table_name: str):
        
        self.query_options.append(ServiceNowQueryOption("table_name",table_name))
        
        return self
    
    def table_sys_id(self, table_sys_id: str):
        
        self.query_options.append(ServiceNowQueryOption("table_sys_id",table_sys_id))
        
        return self
    
    def file_name(self, file_name: str):
        
        self.query_options.append(ServiceNowQueryOption("file_name",file_name))
        
        return self