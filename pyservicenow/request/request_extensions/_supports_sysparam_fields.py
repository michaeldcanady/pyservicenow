"""Houses Supports Sysparam Fields"""

from typing import List
from sys import version_info


from pyservicenow.types.enums import QueryParameters
from pyservicenow.types.models import ServiceNowQueryOption
from pyservicenow.request.request_extensions._supports_query_options import (
    SupportsQueryOptions,
)

if version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self


class SupportsSysparamFields(SupportsQueryOptions):
    """Supports Sysparam Fields Type"""

    def sysparam_fields(self, fields: List[str]) -> Self:
        """Adds the listed fields

        Args:
            fields (List[str]): The fields to be returned

        Returns:
            TableEntryCollectionRequest: The request object to send.
        """

        self._query_options.append(
            ServiceNowQueryOption(QueryParameters.FIELDS, fields)
        )
        return self
