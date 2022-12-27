from typing import List, MutableSequence, Iterator

# internal imports
from pyservicenow.request._base_servicenow_request import BaseServiceNowEntryRequest

class ServiceNowRequestCollection(MutableSequence[BaseServiceNowEntryRequest]):

    def __init__(self) -> None:
        self._internal_list: List[BaseServiceNowEntryRequest] = []

    def append(self, header: BaseServiceNowEntryRequest) -> None:
        self._internal_list.append(header)
    
    def __iter__(self) -> Iterator:

        for value in self.asList():
            yield value.asDict()

    def __batch__(self) -> Iterator:

        for value in self.asList():
            yield value.__batch__()

    def __getitem__(self, index: int) -> BaseServiceNowEntryRequest:
        return self._internal_list[index]

    def __len__(self) -> int:
        return len(self._internal_list)

    def __delitem__(self, index: int) -> None:
        del self._internal_list[index]

    def __setitem__(self, index: int, item: BaseServiceNowEntryRequest) -> None:
        self._internal_list[index] = item
    
    def insert(self, index: int, value: BaseServiceNowEntryRequest) -> None:
        return self._internal_list.insert(index, value)

    def asList(self) -> List[BaseServiceNowEntryRequest]:
        return self._internal_list

    def Json(self) -> dict:
        return{
            "batch_request_id": 1,
            "rest_request": [value.asDict() for value in self.asList()]
        }