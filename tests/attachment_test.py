import os
from pyservicenow.core import ServiceNowClient, UsernamePasswordCredential
from pyservicenow.types.models import QueryBuilder, AttachmentEntry

def test_attachment_url():
    
    creds = UsernamePasswordCredential(os.environ["USERNAME"], os.environ["PASSWORD"])

    client = ServiceNowClient(credential=creds, instance=os.environ["INSTANCE"])

    attachment_request = client.Now().Attachment.request.Get
    
    assert attachment_request.request_url == client.base_url+"/now/attachments"
    

def test_get_first_attachment():
    """tests successfully getting attachment collection
    """
    
    creds = UsernamePasswordCredential(os.environ["USERNAME"], os.environ["PASSWORD"])

    client = ServiceNowClient(credential=creds, instance=os.environ["INSTANCE"])

    attachments = client.Now().Attachment.request.Limit(1).Get.Invoke

    assert type(attachments) == list
    assert type(attachments[0]) == AttachmentEntry