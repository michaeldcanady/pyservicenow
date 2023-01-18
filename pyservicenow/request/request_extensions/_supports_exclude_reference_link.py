"""Houses Supports Exclude Reference Link"""

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


class SupportsExcludeReferenceLink(SupportsQueryOptions):
    """Supports Exclude Reference Link Type"""

    def exclude_reference_link(self, exclude_reference_link: bool) -> Self:
        """Adds if to exclude reference links

        Args:
            exclude_reference_link (bool): If to exclude reference links

        Returns:
            TableEntryCollectionRequest: The request object to send.
        """

        self._query_options.append(
            ServiceNowQueryOption(
                QueryParameters.EXCLUDEREFERENCELINK, exclude_reference_link
            )
        )
        return self
