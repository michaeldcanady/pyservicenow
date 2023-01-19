"""Houses Base Table Request"""

from __future__ import annotations
from typing import TypeVar
from pyservicenow.request._base_servicenow_request import BaseServiceNowEntryRequest
from pyservicenow.types.models._query_builder39 import QueryBuilder
from pyservicenow.types.models import (
    ServiceNowQueryOption,
    ServiceNowEntry,
    ServiceNowHeaderOption,
)

S = TypeVar("S", bound=ServiceNowEntry)


class BaseTableRequest(
    BaseServiceNowEntryRequest[S],
    SupportsSysparamOffset,
    SupportsSysparamLimit,
    SupportsSysparamQuery,
    SupportsExcludeReferenceLink,
    SupportsDisplayValue,
    SupportsSysparamFields,
    SupportsNoCount,
    SupportsSysparamCategory,
    SupportsNoDomain,
    SupportsSuppressPaginationHeader,
    SupportsSysparamView,
):
    """Base Table Request types"""
