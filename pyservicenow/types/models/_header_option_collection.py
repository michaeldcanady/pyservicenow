from typing import MutableSequence, List, Iterator, Dict

# internal import
from pyservicenow.types.models._servicenow_header_option import ServiceNowHeaderOption

class HeaderOptionsCollection(MutableSequence[ServiceNowHeaderOption]):

    def __init__(self) -> None:
        super().__init__()
        self._internal_list: List[ServiceNowHeaderOption] = []

    def append(self, header: ServiceNowHeaderOption) -> None:
        self._internal_list.append(header)
    
    def __iter__(self) -> Iterator:

        for value in self._internal_list:
            yield value.asDict()

    def __getitem__(self, index: int) -> ServiceNowHeaderOption:
        return self._internal_list[index]

    def __len__(self) -> int:
        return len(self._internal_list)

    def __delitem__(self, index: int) -> None:
        del self._internal_list[index]

    def __setitem__(self, index: int, item: ServiceNowHeaderOption) -> None:
        self._internal_list[index] = item
    
    def insert(self, index: int, value: ServiceNowHeaderOption) -> None:
        return self._internal_list.insert(index, value)

    def asList(self) -> List[Dict]:
        return [header.asDict() for header in self._internal_list]