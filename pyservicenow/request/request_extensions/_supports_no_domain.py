"""Houses Supports No Domain"""

from typing import TypeVar


from pyservicenow.types.enums import QueryParameters
from pyservicenow.types.models import ServiceNowQueryOption
from pyrestsdk.request.supports_types import SupportsQueryOptions

S = TypeVar("S", bound="SupportsNoDomain")


class SupportsNoDomain(SupportsQueryOptions):
    """Supports No Domain type"""

    def no_domain(self: S, no_domain: bool) -> S:
        """Flag that indicates whether to restrict the record
        search to only the domains for which the logged in user is configured.

        Args:
            no_domain (bool): whether to restrict the record search to only
            the domains for which the logged in user is configured.

        Returns:
            TableEntryCollectionRequest: The request object to send.
        """

        self.query_options.append(
            ServiceNowQueryOption(QueryParameters.NODOMAIN, no_domain)
        )
        return self
