"""Table Tests"""

import os

from pyrestsdk.credential import BasicCredential

from pyservicenow.core import ServiceNowClient
from pyservicenow.types.models import ServiceNowEntry

def test_table_url():
    """tests if the table url is generated property
    """

    creds = BasicCredential(os.environ["USERNAME"], os.environ["PASSWORD"])

    client = ServiceNowClient(credential=creds, instance=os.environ["INSTANCE"])

    table_name = "alm_hardware"

    hardware_request = client.Now.v2.table_api(table_name).request.sysparam_limit(1).Get

    assert hardware_request.request_url == client.base_url+"/now/table/"+table_name


def test_get_one_element():
    """tests successfully getting table collection with one object
    """

    creds = BasicCredential(os.environ["USERNAME"], os.environ["PASSWORD"])

    client = ServiceNowClient(credential=creds, instance=os.environ["INSTANCE"])

    hardware = client.Now.v2.table_api("alm_hardware").request.sysparam_limit(1).Get.invoke_request

    assert isinstance(hardware, list)
    assert isinstance(hardware[0], ServiceNowEntry)