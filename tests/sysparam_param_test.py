import os

from pyrestsdk.credential import BasicCredential

from pyservicenow.core import ServiceNowClient

from pyservicenow.types.enums import DisplayValue, View

from pyservicenow.types.models import QueryBuilder

def test_sysparam_fields():

    creds = BasicCredential(os.environ["USERNAME"], os.environ["PASSWORD"])

    client = ServiceNowClient(credential=creds, instance=os.environ["INSTANCE"])

    request = client.Now.v2.table_api("alm_hardware").request.sysparam_fields(
        lambda x: [x.sys_created_on, x.sys_updated_on]
    )

    assert (
        str(request.query_options) == "sysparm_fields=sys_created_on%2Csys_updated_on"
    )


def test_exclude_reference_link():

    creds = BasicCredential(os.environ["USERNAME"], os.environ["PASSWORD"])

    client = ServiceNowClient(credential=creds, instance=os.environ["INSTANCE"])

    request = client.Now.v2.table_api("alm_hardware").request.exclude_reference_link(
        True
    )

    assert str(request.query_options) == "sysparm_exclude_reference_link=true"


def test_display_value():

    creds = BasicCredential(os.environ["USERNAME"], os.environ["PASSWORD"])

    client = ServiceNowClient(credential=creds, instance=os.environ["INSTANCE"])

    request = client.Now.v2.table_api("alm_hardware").request.display_value(
        DisplayValue.ALL
    )

    assert str(request.query_options) == "sysparm_display_value=all"


def test_no_count():

    creds = BasicCredential(os.environ["USERNAME"], os.environ["PASSWORD"])

    client = ServiceNowClient(credential=creds, instance=os.environ["INSTANCE"])

    request = client.Now.v2.table_api("alm_hardware").request.no_count(False)

    assert str(request.query_options) == "sysparm_no_count=false"


def test_suppress_pagination_header():

    creds = BasicCredential(os.environ["USERNAME"], os.environ["PASSWORD"])

    client = ServiceNowClient(credential=creds, instance=os.environ["INSTANCE"])

    request = client.Now.v2.table_api(
        "alm_hardware"
    ).request.suppress_pagination_header(False)

    assert str(request.query_options) == "sysparm_suppress_pagination_header=false"


def test_sysparam_limit():

    creds = BasicCredential(os.environ["USERNAME"], os.environ["PASSWORD"])

    client = ServiceNowClient(credential=creds, instance=os.environ["INSTANCE"])

    request = client.Now.v2.table_api("alm_hardware").request.sysparam_limit(1)

    assert str(request.query_options) == "sysparm_limit=1"


def test_sysparam_offset():

    creds = BasicCredential(os.environ["USERNAME"], os.environ["PASSWORD"])

    client = ServiceNowClient(credential=creds, instance=os.environ["INSTANCE"])

    request = client.Now.v2.table_api("alm_hardware").request.sysparam_offset(1)

    assert str(request.query_options) == "sysparm_offset=1"


def test_sysparam_query():

    creds = BasicCredential(os.environ["USERNAME"], os.environ["PASSWORD"])

    client = ServiceNowClient(credential=creds, instance=os.environ["INSTANCE"])
    
    query = QueryBuilder().field("serial").equals("92XWKW2")

    request = client.Now.v2.table_api("alm_hardware").request.sysparam_query(query)
    
    assert str(request.query_options) == "sysparm_query=serial=92XWKW2"

def test_sysparam_view():

    creds = BasicCredential(os.environ["USERNAME"], os.environ["PASSWORD"])

    client = ServiceNowClient(credential=creds, instance=os.environ["INSTANCE"])

    request = client.Now.v2.table_api("alm_hardware").request.sysparam_view(View.BOTH)
    
    assert str(request.query_options) == "sysparm_view=both"