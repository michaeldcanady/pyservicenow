from sys import version_info

from enum import IntEnum, auto
from typing import Union, List
import inspect

from strenum import StrEnum

# internal imports
from ..exceptions import (
    QueryEmpty,
    QueryExpressionError,
    QueryMissingField,
    QueryMultipleExpressions,
)

if version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self


class OrderBy(IntEnum):
    ASC = auto()
    DESC = auto()


class Operators(StrEnum):
    Null = ""
    Equals = "="
    In = "IN"
    Contains = "LIKE"


class LogicalOperator(StrEnum):
    And = "^"
    Or = "^OR"
    NewQuery = "^NQ"


class QueryBuilder:

    __slots__ = ["_query", "current_field", "c_oper", "l_oper"]

    def __init__(self) -> None:
        """Constructs a new query builder"""

        self._query = []
        self.current_field = None
        self.c_oper = None
        self.l_oper = None

    @classmethod
    def parse(cls, query: str) -> Self:
        """Parses query into new QueryBuilder

        Args:
            query (str): The query to parse

        Returns:
            QueryBuilder: The new QueryBuilder object
        """

        query_builder = cls()

        field = ""
        operator = Operators.Null
        value = ""

        i, l = 0, len(query)

        while i < l:

            match (query):
                case n if (n[i] == Operators.Equals) or (
                    n[i : i + 1] == Operators.In
                ) or (n[i : i + 4] == Operators.Contains):
                    query_builder.field(field)
                    if query[i] == Operators.Equals:
                        operator = Operators.Equals
                    elif query[i : i + 2] == Operators.In:
                        i += 2
                        operator = Operators.In
                        continue
                    elif query[i : i + 4] == Operators.Contains:
                        i += 4
                        operator = Operators.Contains
                        continue
                    field = ""
                case n if n[i] == "^":

                    match (operator):
                        case Operators.Equals:
                            query_builder.equals(value)
                        case Operators.In:
                            query_builder.IN(value)
                        case Operators.Contains:
                            query_builder.contains(value)

                    if query[i : i + 4] == LogicalOperator.NewQuery:
                        query_builder.NQ
                        i += 4
                        continue
                    elif query[i : i + 4] == LogicalOperator.Or:
                        query_builder.OR
                        i += 4
                        continue
                    else:
                        query_builder.AND

                    value = ""
                    operator = Operators.Null

                case _ if operator != Operators.Null:
                    value += query[i]
                    if i == l - 1:
                        match (operator):
                            case Operators.Equals:
                                query_builder.equals(value)
                            case Operators.In:
                                query_builder.IN(value)
                            case Operators.Contains:
                                query_builder.contains(value)
                case other:
                    field += query[i]

            i += 1

        return query_builder

    def field(self, field: str) -> Self:
        """Sets the field to operate on

        Args:
            field (str): The field

        Returns:
            QueryBuilder: The query builder
        """

        self.current_field = field

        return self

    def orderBy(self, direction: OrderBy) -> Self:
        """Sets the order by direction

        Args:
            direction (OrderBy): Direction to order results by

        Raises:
            Exception: _description_
            Exception: _description_

        Returns:
            QueryBuilder: The current QueryBuilder object
        """

        if direction == OrderBy.ASC:
            self._query.append("ORDERBY{0}".format(self.current_field))
        elif direction == OrderBy.DESC:
            self._query.append("ORDERBYDESC{0}".format(self.current_field))

        if (_currentframe := inspect.currentframe()) is None:
            raise Exception("Current Frame is None")

        if (_f_back := _currentframe.f_back) is None:
            raise Exception("f_back is None")

        self.c_oper = _f_back.f_code.co_name

        return self

    def equals(self, data: Union[str, int]) -> Self:

        return self._add_condition(Operators.Equals, data, types=[int, str])

    def IN(self, data: List) -> Self:
        return self._add_condition("IN", ",".join(map(str, data)), types=[str])

    def contains(self, contains) -> Self:
        """Adds new `LIKE` condition
        :param contains: Match field containing the provided value
        """

        return self._add_condition("LIKE", contains, types=[str])

    @property
    def AND(self) -> Self:
        """Adds an and-operator"""
        return self._add_logical_operator(LogicalOperator.And)

    @property
    def OR(self) -> Self:
        """Adds an or-operator"""
        return self._add_logical_operator(LogicalOperator.Or)

    @property
    def NQ(self) -> Self:
        """Adds a NQ-operator (new query)"""
        return self._add_logical_operator(LogicalOperator.NewQuery)

    def __str__(self) -> str:
        """String representation of the query object
        :raise:
            - QueryEmpty: if there's no conditions defined
            - QueryMissingField: if field() hasn't been set
            - QueryExpressionError: if a expression hasn't been set
        :return:
            - String-type query
        """

        if len(self._query) == 0:
            raise QueryEmpty("At least one condition is required")
        elif self.current_field is None:
            raise QueryMissingField("Logical operator expects a field()")
        elif self.c_oper is None:
            raise QueryExpressionError("field() expects an expression")

        return str().join(self._query)

    def _add_logical_operator(self, operator: LogicalOperator) -> Self:
        """Adds a logical operator in query
        :param operator: logical operator (str)
        :raise:
            - QueryExpressionError: if a expression hasn't been set
        """

        if not self.c_oper:
            raise QueryExpressionError(
                "Logical operators must be preceded by an expression"
            )

        self.current_field = None
        self.c_oper = None

        if (_currentframe := inspect.currentframe()) is None:
            raise Exception("Current Frame is None")

        if (_f_back := _currentframe.f_back) is None:
            raise Exception("f_back is None")

        self.l_oper = _f_back.f_code.co_name

        self._query.append(operator)
        return self

    def _add_condition(self, operator, operand, types) -> Self:
        """Appends condition to self._query after performing validation
        :param operator: operator (str)
        :param operand: operand
        :param types: allowed types
        :raise:
            - QueryMissingField: if a field hasn't been set
            - QueryMultipleExpressions: if a condition already has been set
            - QueryTypeError: if the value is of an unexpected type
        """

        if not self.current_field:
            raise QueryMissingField("Conditions requires a field()")

        # elif not type(operand) in types:
        #    caller = inspect.currentframe().f_back.f_code.co_name
        #    raise QueryTypeError(
        #        "Invalid type passed to %s() , expected: %s" % (caller, types)
        #    )

        elif self.c_oper:
            raise QueryMultipleExpressions("Expected logical operator after expression")

        if (_currentframe := inspect.currentframe()) is None:
            raise Exception("Current Frame is None")

        if (_f_back := _currentframe.f_back) is None:
            raise Exception("f_back is None")

        self.c_oper = _f_back.f_code.co_name

        self._query.append(
            "%(current_field)s%(operator)s%(operand)s"
            % {
                "current_field": self.current_field,
                "operator": operator,
                "operand": operand,
            }
        )

        return self
