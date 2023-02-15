"""Houses Supports Sysparam Fields"""

from typing import List, TypeVar, Type, Callable

from pyrestsdk.request.supports_types import SupportsGenericType, SupportsQueryOptions

from pyservicenow.types.enums import QueryParameters
from pyservicenow.types.models import ServiceNowQueryOption

S = TypeVar("S", bound="SupportsSysparamFields")
T = TypeVar("T")


class SupportsSysparamFields(SupportsQueryOptions, SupportsGenericType):
    """Supports Sysparam Fields Type"""

    def sysparam_fields(self: S, fields: List[str]) -> S:
        """Sets the sysparam fields query option

        Args:
            self (S): SupportsSysparamFields instance
            fields (List[str]): The list of fields to add

        Returns:
            S: SupportsSysparamFields instance
        """

        self.query_options.append(ServiceNowQueryOption(QueryParameters.FIELDS, fields))

        return self


def get_properties(
    expression: Callable[[Type[T]], List[property]], type_of: Type[T]
) -> List[str]:

    raw_properties = expression(type_of)

    return [prop.fget.__name__ for prop in raw_properties if prop.fget is not None]
