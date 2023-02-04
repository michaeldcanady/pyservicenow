# PyServiceNow

## Distributing
Check any of the Release/* branches to find the needed version
Check under dist for the .whl file

```bash
pip install *.whl
```

## Making Wheel
```bash
python setup.py bdist_wheel --universal
```

## Example Basic Call
```python
from pyservicenow.core import UsernamePasswordCredential, ServiceNowClient
from pyservicenow.types.models.querybuilder import QueryBuilder

credential = UsernamePasswordCredential("", "")

client = ServiceNowClient(credential=credential, instance="instance")

query = QueryBuilder().field("serial_number").equals("92XWKW2")

Ticket = client.Now.table_api("alm_hardware").Request.sysparam_query(query).sysparam_limit(1).Get.invoke_request
```