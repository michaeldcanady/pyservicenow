"""Houses query parameter enum"""

from strenum import StrEnum


class QueryParameters(StrEnum):
    """Query Parameters enum"""

    EXCLUDEREFERENCELINK = "sysparm_exclude_reference_link"
    FIELDS = "sysparm_fields"
    LIMIT = "sysparm_limit"
    NOCOUNT = "sysparm_no_count"
    OFFSET = "sysparm_offset"
    QUERY = "sysparm_query"
    CATEGORY = "sysparm_query_category"
    NODOMAIN = "sysparm_query_no_domain"
    VIEW = "sysparm_view"
    SUPPRESSPAGINATIONHEADER = "sysparm_suppress_pagination_header"
    DISPLAYVALUE = "sysparm_display_value"
