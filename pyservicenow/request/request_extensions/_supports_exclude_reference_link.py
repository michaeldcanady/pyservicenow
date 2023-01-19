"""Houses Supports Exclude Reference Link"""

from typing import TypeVar

from pyservicenow.types.enums import QueryParameters
from pyservicenow.types.models import ServiceNowQueryOption
from pyservicenow.request.request_extensions._supports_query_options import (
    SupportsQueryOptions,
)

S = TypeVar("S", bound="SupportsExcludeReferenceLink")


class SupportsExcludeReferenceLink(SupportsQueryOptions):
    """Supports Exclude Reference Link Type"""

    def exclude_reference_link(self: S, exclude_reference_link: bool) -> S:
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
