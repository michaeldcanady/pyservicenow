import os

from pyrestsdk.credential import BasicCredential

from pyservicenow.core import ServiceNowClient
from pyservicenow.types.models import AttachmentEntry

def test_current_url():

    creds = BasicCredential(os.environ["USERNAME"], os.environ["PASSWORD"])

    client = ServiceNowClient(credential=creds, instance=os.environ["INSTANCE"])

    attachment_request = client.Now.v2.ui_api.User.current_user
    
    assert attachment_request.request_url == client.base_url+"/now/ui/user/current_user"