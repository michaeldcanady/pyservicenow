"""Houses Supports Sysparam Category"""

from typing import TypeVar


from pyservicenow.types.enums import QueryParameters
from pyservicenow.types.models import ServiceNowQueryOption
from pyrestsdk.request.supports_types import SupportsQueryOptions

S = TypeVar("S", bound="SupportsSysparamCategory")


class SupportsSysparamCategory(SupportsQueryOptions):
    """Supports Sysparam Category Type"""

    def sysparam_category(self: S, category: str) -> S:
        """Name of the category to use for queries.

        Args:
            category (str): Name of the category.

        Returns:
            TableEntryCollectionRequest: The request object to send.
        """

        self.query_options.append(
            ServiceNowQueryOption(QueryParameters.CATEGORY, category)
        )
        return self
