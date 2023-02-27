"""Houses Abstract Base Query Builder"""

from typing import Union, List, TypeVar, Any

from abc import abstractmethod

import inspect

from pyservicenow.types.enums import OrderBy, Operators

from ..exceptions import (
    QueryEmpty,
    QueryExpressionError,
    QueryMissingField,
    QueryMultipleExpressions,
)

Q = TypeVar("Q", bound="AbstractBaseQueryBuilder")


class AbstractBaseQueryBuilder:
    """Abstract Base Query Builder Type"""

    @abstractmethod
    def field(self: Q, field: str) -> Q:
        """Sets the field to operate on

        Args:
            self (Q): The query builder
            field (str): The field

        Returns:
            Q: The query builder
        """

    @abstractmethod
    def equals(self: Q, data: Union[str, int]) -> Q:
        """Sets the operator to equals

        Args:
            self (Q): The query builder
            data (Union[str, int]): Value the field should equal

        Returns:
            Q: The query builder
        """

    @abstractmethod
    def order_by(self: Q, direction: OrderBy) -> Q:
        """Sets the order by direction

        Args:
            self (Q): The query builder
            direction (OrderBy): Direction to order results by

        Raises:
            Exception: _description_
            Exception: _description_

        Returns:
            QueryBuilder: The current QueryBuilder object
        """

    @abstractmethod
    def IN(self: Q, data: List) -> Q:
        """Sets the operator to in

        Args:
            self (Q): The query builder
            data (List): The value to see if the field's value is in

        Returns:
            Q: The query builder
        """

    @property
    @abstractmethod
    def AND(self: Q) -> Q:
        """Adds an and-operator"""

    @property
    @abstractmethod
    def OR(self: Q) -> Q:
        """Adds an or-operator"""

    @property
    @abstractmethod
    def NQ(self: Q) -> Q:
        """Adds a NQ-operator (new query)"""

    @abstractmethod
    def contains(self: Q, contains) -> Q:
        """Adds new `LIKE` condition

        Args:
            self (Q): The query builder
            contains (_type_): Match field containing the provided value

        Returns:
            Q: The query builder
        """

    @abstractmethod
    def _add_logical_operator(self: Q, operator: Operators.Logical) -> Q:
        """Adds a logical operator in query

        Args:
            self (Q): The query builder
            operator (Operators.Logical): logical operator

        Raises:
            - QueryExpressionError: if a expression hasn't been set

        Returns:
            Q: The query builder
        """

    @abstractmethod
    def _add_condition(
        self: Q, operator: Operators.Comparison, operand: Any, types: List[Any]
    ) -> Q:
        """Appends condition to self._query after performing validation

        Args:
            self (Q): The query builder
            operator (Operators.Comparison): Comparison operator for the condition
            operand (Any): operand for the condition
            types (List[Any]): Allowed types

        Raises:
            - QueryMissingField: if a field hasn't been set
            - QueryMultipleExpressions: if a condition already has been set
            - QueryTypeError: if the value is of an unexpected type

        Returns:
            Q: The query builder
        """
