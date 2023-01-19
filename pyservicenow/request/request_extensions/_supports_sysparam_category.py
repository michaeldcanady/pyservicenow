"""Houses Supports Sysparam Category"""

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


class SupportsSysparamCategory(SupportsQueryOptions):
    """Supports Sysparam Category Type"""

    def sysparam_category(self, category: str) -> Self:
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
