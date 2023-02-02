"""Houses Supports Display Value"""

from typing import TypeVar


from pyservicenow.types.enums import QueryParameters, DisplayValue
from pyservicenow.types.models import ServiceNowQueryOption
from pyrestsdk.request.supports_types import SupportsQueryOptions

S = TypeVar("S", bound="SupportsDisplayValue")


class SupportsDisplayValue(SupportsQueryOptions):
    """Supports Display Value Type"""

    def display_value(self: S, values: DisplayValue) -> S:
        """Sets the sysparm_display_value

        Args:
            values (DisplayValue): The display values

        Returns:
            TableEntryCollectionRequest: The request object to send.
        """

        self.query_options.append(
            ServiceNowQueryOption(QueryParameters.DISPLAYVALUE, str(values))
        )
        return self
