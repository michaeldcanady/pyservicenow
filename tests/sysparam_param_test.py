"""Sysparam tests"""

import os

from pyrestsdk.credential import BasicCredential

from pyservicenow.core import ServiceNowClient

from pyservicenow.types.enums import DisplayValue, View

from pyservicenow.types.models import QueryBuilder


def test_sysparam_fields():
    """Testing that lambda builds query options properly"""

    creds = BasicCredential(os.environ["USERNAME"], os.environ["PASSWORD"])

    client = ServiceNowClient(credential=creds, instance=os.environ["INSTANCE"])

    request = client.Now.v2.table_api("alm_hardware").request.sysparam_fields(
        lambda x: [x.sys_created_on, x.sys_updated_on]
    )

    assert (
        str(request.query_options) == "sysparm_fields=sys_created_on%2Csys_updated_on"
    )


def test_exclude_reference_link():
    """Testing exclude reference link query option"""

    creds = BasicCredential(os.environ["USERNAME"], os.environ["PASSWORD"])

    client = ServiceNowClient(credential=creds, instance=os.environ["INSTANCE"])

    request = client.Now.v2.table_api("alm_hardware").request.exclude_reference_link(
        True
    )

    assert str(request.query_options) == "sysparm_exclude_reference_link=True"


def test_display_value():
    """Testing display value query option"""

    creds = BasicCredential(os.environ["USERNAME"], os.environ["PASSWORD"])

    client = ServiceNowClient(credential=creds, instance=os.environ["INSTANCE"])

    request = client.Now.v2.table_api("alm_hardware").request.display_value(
        DisplayValue.ALL
    )

    assert str(request.query_options) == "sysparm_display_value=all"


def test_no_count():
    """Testing no count query option"""

    creds = BasicCredential(os.environ["USERNAME"], os.environ["PASSWORD"])

    client = ServiceNowClient(credential=creds, instance=os.environ["INSTANCE"])

    request = client.Now.v2.table_api("alm_hardware").request.no_count(False)

    assert str(request.query_options) == "sysparm_no_count=False"


def test_suppress_pagination_header():
    """Testing suppress pagination header query option"""

    creds = BasicCredential(os.environ["USERNAME"], os.environ["PASSWORD"])

    client = ServiceNowClient(credential=creds, instance=os.environ["INSTANCE"])

    request = client.Now.v2.table_api(
        "alm_hardware"
    ).request.suppress_pagination_header(False)

    assert str(request.query_options) == "sysparm_suppress_pagination_header=False"


def test_sysparam_limit():
    """Testing sysparam limit query option"""

    creds = BasicCredential(os.environ["USERNAME"], os.environ["PASSWORD"])

    client = ServiceNowClient(credential=creds, instance=os.environ["INSTANCE"])

    request = client.Now.v2.table_api("alm_hardware").request.sysparam_limit(1)

    assert str(request.query_options) == "sysparm_limit=1"


def test_sysparam_offset():
    """Testing sysparam offset query option"""

    creds = BasicCredential(os.environ["USERNAME"], os.environ["PASSWORD"])

    client = ServiceNowClient(credential=creds, instance=os.environ["INSTANCE"])

    request = client.Now.v2.table_api("alm_hardware").request.sysparam_offset(1)

    assert str(request.query_options) == "sysparm_offset=1"


def test_sysparam_query():
    """Testing sysparam query query option"""

    creds = BasicCredential(os.environ["USERNAME"], os.environ["PASSWORD"])

    client = ServiceNowClient(credential=creds, instance=os.environ["INSTANCE"])

    query = QueryBuilder().field("serial").equals("92XWKW2")

    request = client.Now.v2.table_api("alm_hardware").request.sysparam_query(query)

    assert str(request.query_options) == "sysparm_query=serial%3D92XWKW2"


def test_sysparam_view():
    """Testing sysparam view query option"""

    creds = BasicCredential(os.environ["USERNAME"], os.environ["PASSWORD"])

    client = ServiceNowClient(credential=creds, instance=os.environ["INSTANCE"])

    request = client.Now.v2.table_api("alm_hardware").request.sysparam_view(View.BOTH)

    assert str(request.query_options) == "sysparm_view=both"
