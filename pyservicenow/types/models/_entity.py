import typing


class Entity():

    def __init__(self):
        self._sys_id: str = ""

    @property
    def SysId(self) -> str:
        return self._sys_id

    @classmethod
    def FromJson(cls, json: dict) -> 'Entity':

        new = cls()

        new._sys_id = json.get("sys_id", "")

        return new

    def __eq__(self, __o: 'Entity') -> bool:
        
        if __o == None:
            return False

        return self.SysId == __o.SysId

    def __hash__(self) -> int:
        
        return hash(self.SysId)