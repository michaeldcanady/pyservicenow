from strenum import StrEnum


class QueryParameters(StrEnum):

    ExcludeReferenceLink = "sysparm_exclude_reference_link"
    Fields = "sysparm_fields"
    Limit = "sysparm_limit"
    NoCount = "sysparm_no_count"
    Offset = "sysparm_offset"
    Query = "sysparm_query"
    Category = "sysparm_query_category"
    NoDomain = "sysparm_query_no_domain"
    View = "sysparm_view"
    SuppressPaginationHeader = "sysparm_suppress_pagination_header"
    DisplayValue = "sysparm_display_value"
