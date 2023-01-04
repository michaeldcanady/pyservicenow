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

Ticket = client.Now().Table("alm_hardware").Request.Query(str(query)).Limit(1).Get.Invoke
```