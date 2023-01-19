import os
from pyservicenow.core import ServiceNowClient
from pyservicenow.core.credential import UsernamePasswordCredential
from pyservicenow.types.models import AttachmentEntry


def test_attachment_url():

    creds = UsernamePasswordCredential(os.environ["USERNAME"], os.environ["PASSWORD"])

    client = ServiceNowClient(credential=creds, instance=os.environ["INSTANCE"])

    attachment_request = client.Now.v2.attachment_api.request.Get
    
    assert attachment_request.request_url == client.base_url+"/now/attachment"
    

def test_get_first_attachment():
    """tests successfully getting attachment collection"""

    creds = UsernamePasswordCredential(os.environ["USERNAME"], os.environ["PASSWORD"])

    client = ServiceNowClient(credential=creds, instance=os.environ["INSTANCE"])

    attachments = client.Now.v2.attachment_api.request.sysparam_limit(1).Get.invoke_request

    assert isinstance(attachments, list)
    assert isinstance(attachments[0], AttachmentEntry)
