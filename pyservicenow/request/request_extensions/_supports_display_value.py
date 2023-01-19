"""Houses Supports Display Value"""

from sys import version_info


from pyservicenow.types.enums import QueryParameters, DisplayValue
from pyservicenow.types.models import ServiceNowQueryOption
from pyservicenow.request.request_extensions._supports_query_options import (
    SupportsQueryOptions,
)

if version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self


class SupportsDisplayValue(SupportsQueryOptions):
    """Supports Display Value Type"""

    def display_value(self, values: DisplayValue) -> Self:
        """Sets the sysparm_display_value

        Args:
            values (DisplayValue): The display values

        Returns:
            TableEntryCollectionRequest: The request object to send.
        """

        self._query_options.append(
            ServiceNowQueryOption(QueryParameters.DISPLAYVALUE, str(values))
        )
        return self
