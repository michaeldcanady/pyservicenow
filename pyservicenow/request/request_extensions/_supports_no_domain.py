"""Houses Supports No Domain"""

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


class SupportsNoDomain(SupportsQueryOptions):
    """Supports No Domain type"""

    def no_domain(self, no_domain: bool) -> Self:
        """Flag that indicates whether to restrict the record
        search to only the domains for which the logged in user is configured.

        Args:
            no_domain (bool): whether to restrict the record search to only
            the domains for which the logged in user is configured.

        Returns:
            TableEntryCollectionRequest: The request object to send.
        """

        self._query_options.append(
            ServiceNowQueryOption(QueryParameters.NODOMAIN, no_domain)
        )
        return self
