from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union


class TableRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the table singleton.
    """

    def __init__(
        self,
        request_adapter: RequestAdapter,
        url_template: str,
        path_parameters: Optional[Union[Dict[str, Any], str]] = None,
    ) -> None:
        super().__init__(request_adapter, "{+baseurl}/table/{table}", path_parameters)

    async def get(
        self,
        request_configuration: Optional[
            TableRequestBuilderGetRequestConfiguration
        ] = None,
    ) -> Optional[Dict[str, Any]]:
        """
        Get table
        Args:
            request_configuration: Configuration for the request such as headers, query
            parameters, and middleware options.
        Returns: Optional[Dict[str, Any]]
        """

        request_info = self.to_get_request_information(request_configuration)

        error_mapping: Dict[str, ParsableFactory] = {}
        if not self.request_adapter:
            raise Exception("Http core is null")

        return await self.request_adapter.send_async(
            request_info, Dict[str, Any], error_mapping
        )

    async def post(
        self,
        body: Optional[Dict[str, Any]],
        request_configuration: Optional[
            TableRequestBuilderPostRequestConfiguration
        ] = None,
    ) -> Optional[Dict[str, Any]]:
        ...

    def to_get_request_information(
        self,
        request_configuration: Optional[
            TableRequestBuilderGetRequestConfiguration
        ] = None,
    ) -> RequestInformation:
        """
        Get table
        Args:
            request_configuration: Configuration for the request such as headers,
            query parameters, and middleware options.
        Returns: RequestInformation
        """

        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(
                request_configuration.query_parameters
            )
            request_info.add_request_options(request_configuration.options)
        return request_info

    def to_post_request_information(
        self,
        body: Optional[Dict[str, Any]],
        request_configuration: Optional[
            TableRequestBuilderPostRequestConfiguration
        ] = None,
    ) -> RequestInformation:
        ...

    @dataclass
    class TableRequestBuilderGetQueryParameters:
        """ """

        def get_query_parameter(self, original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template
            parsing.
            Args:
                original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "display_value":
                return "sysparm_display_value"
            if original_name == "exclude_reference_link":
                return "sysparm_exclude_reference_link"
            if original_name == "fields":
                return "sysparm_fields"
            if original_name == "limit":
                return "sysparam_limit"
            if original_name == "no_count":
                return "sysparm_no_count"
            if original_name == "offset":
                return "sysparam_offset"
            if original_name == "query":
                return "sysparam_query"
            if original_name == "query_category":
                return "sysparam_query_category"
            if original_name == "query_no_domain":
                return "sysparm_query_no_domain"
            if original_name == "suppress_pagination_header":
                return "sysparm_suppress_pagination_header"
            if original_name == "view":
                return "sysparm_view"
            return original_name

        # true, false, all
        display_value: str = "false"
        exclude_reference_link: bool = False
        fields: Optional[List[str]] = None
        limit: int = 1000
        no_count: bool = False
        offset: int = 0
        query: Optional[str] = None
        query_category: Optional[str] = None
        query_no_domain: bool = False
        suppress_pagination_header: bool = False
        # desktop mobile both
        view: Optional[str] = None

    @dataclass
    class TableRequestBuilderPostQueryParameters:
        ...

    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class TableRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        """ """

        query_parameters: Optional[
            TableRequestBuilder.TableRequestBuilderGetQueryParameters
        ] = None

    @dataclass
    class TableRequestBuilderPostRequestConfiguration(BaseRequestConfiguration):
        """ """

        query_parameters: Optional[
            TableRequestBuilder.TableRequestBuilderPostQueryParameters
        ] = None
