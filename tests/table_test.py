import os
from pyservicenow.core import ServiceNowClient, UsernamePasswordCredential
from pyservicenow.types.models import QueryBuilder, AttachmentEntry, ServiceNowEntry

def test_attachment_url():
    
    creds = UsernamePasswordCredential(os.environ["USERNAME"], os.environ["PASSWORD"])

    client = ServiceNowClient(credential=creds, instance=os.environ["INSTANCE"])
    
    table_name = "alm_hardware"

    hardware_request = client.Now().Table(table_name).request.sysparam_limit(1).Get
    
    assert hardware_request.request_url == client.base_url+"/now/table/"+table_name
    

def test_get_first_attachment():
    """tests successfully getting attachment collection
    """
    
    creds = UsernamePasswordCredential(os.environ["USERNAME"], os.environ["PASSWORD"])

    client = ServiceNowClient(credential=creds, instance=os.environ["INSTANCE"])

    hardware = client.Now().Table("alm_hardware").request.Limit(1).Get.Invoke

    assert type(hardware) == list
    assert type(hardware[0]) == ServiceNowEntry