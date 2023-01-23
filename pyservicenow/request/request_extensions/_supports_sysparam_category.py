"""Houses Supports Sysparam Category"""

from typing import TypeVar


from pyservicenow.types.enums import QueryParameters
from pyservicenow.types.models import ServiceNowQueryOption
from pyservicenow.request.request_extensions._supports_query_options import (
    SupportsQueryOptions,
)

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

        self._query_options.append(
            ServiceNowQueryOption(QueryParameters.CATEGORY, category)
        )
        return self
