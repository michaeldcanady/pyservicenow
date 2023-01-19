"""Houses Supports Sysparam View"""

from sys import version_info


from pyservicenow.types.enums import QueryParameters, View
from pyservicenow.types.models import ServiceNowQueryOption
from pyservicenow.request.request_extensions._supports_query_options import (
    SupportsQueryOptions,
)

if version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self


class SupportsSysparamView(SupportsQueryOptions):
    """Supports Query Options Type"""

    def sysparam_view(self, view: View) -> Self:
        """UI view for which to render the data. Determines the fields returned in the response.

        Args:
            view (View): The view.

        Returns:
            TableEntryCollectionRequest: The request object to send.
        """

        self._query_options.append(ServiceNowQueryOption(QueryParameters.VIEW, view))
        return self
