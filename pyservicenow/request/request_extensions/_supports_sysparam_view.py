"""Houses Supports Sysparam View"""

from typing import TypeVar


from pyservicenow.types.enums import QueryParameters, View
from pyservicenow.types.models import ServiceNowQueryOption
from pyrestsdk.request.supports_types import SupportsQueryOptions

S = TypeVar("S", bound="SupportsSysparamView")


class SupportsSysparamView(SupportsQueryOptions):
    """Supports Query Options Type"""

    def sysparam_view(self: S, view: View) -> S:
        """UI view for which to render the data. Determines the fields returned in the response.

        Args:
            view (View): The view.

        Returns:
            TableEntryCollectionRequest: The request object to send.
        """

        self.query_options.append(ServiceNowQueryOption(QueryParameters.VIEW, view))
        return self
