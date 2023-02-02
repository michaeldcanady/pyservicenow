"""Houses Supports Sysparam Fields"""

from typing import List, TypeVar


from pyservicenow.types.enums import QueryParameters
from pyservicenow.types.models import ServiceNowQueryOption
from pyrestsdk.request.supports_types import SupportsQueryOptions

S = TypeVar("S", bound="SupportsSysparamFields")


class SupportsSysparamFields(SupportsQueryOptions):
    """Supports Sysparam Fields Type"""

    def sysparam_fields(self: S, fields: List[str]) -> S:
        """Adds the listed fields

        Args:
            fields (List[str]): The fields to be returned

        Returns:
            TableEntryCollectionRequest: The request object to send.
        """

        self.query_options.append(
            ServiceNowQueryOption(QueryParameters.FIELDS, fields)
        )
        return self
