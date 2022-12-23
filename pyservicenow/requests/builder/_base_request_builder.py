from typing import Any

class BaseRequestBuilder:
    
    _client: Any
    _request_url: str
    
    def __init__(self, request_url: str, client) -> None:
        self._client = client
        self._request_url = request_url
        
    @property
    def Client(self):
        return self._client
    
    @property
    def RequestUrl(self) -> str:
        return self._request_url
    
    def AppendSegmentToRequestUrl(self, url_segment:str) -> str:
        """Gets a URL that is the request builder's request URL with the segment appended.

        Args:
            url_segment (str): The segment to append to the request URL.

        Returns:
            str: A URL that is the request builder's request URL with the segment appended.
        """
        
        if not url_segment.startswith("/"):
            # Checks if url segment starts with /
            # Appends it if it does not
            url_segment = "/{0}".format(url_segment)
        
        return "{0}{1}".format(self.RequestUrl, url_segment)