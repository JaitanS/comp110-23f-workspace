"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730675117"


class Simpy:
    """Class for assignment."""
    values: list[float]

    def __init__(self, values: list[float]) -> None:
        """Constructs class Simpy."""
        self.values = values
    
    def __str__(self) -> str: 
        """Creates a readable string."""
        return f"Simpy({self.values})"
    
    def fill(self, float: float, int: int) -> None:
        """Fills Simpy's values."""
        x: int = 0
        simpy_list: list[float] = []
        while x < int: 
            simpy_list.append(float)
            x += 1
        self.values = simpy_list

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill values with range of floats."""
        assert step != 0.0
        simpy_list: list[float] = []
        x: float = start
        while abs(x) < abs(stop): 
            simpy_list.append(x)
            x += step
        self.values = simpy_list

    def sum(self) -> float: 
        """Sums the values in Simpy."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Uses the + operator to add simpy objects and floats."""
        simpy_values = Simpy([])
        simpy_values.fill(0.0, len(self.values))
        if type(rhs) is type(self): 
            assert len(self.values) == len(rhs.values)
            x: int = 0
            while x < len(self.values): 
                simpy_values.values[x] = self.values[x] + rhs.values[x]
                x += 1
        elif type(rhs) is float: 
            x: int = 0
            while x < len(self.values): 
                simpy_values.values[x] = self.values[x] + rhs
                x += 1
        return simpy_values

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy: 
        """Puts a list of values to the power of another."""
        simpy_values = Simpy([])
        simpy_values.fill(0.0, len(self.values))
        if type(rhs) is type(self): 
            assert len(self.values) == len(rhs.values)
            x: int = 0
            while x < len(self.values): 
                simpy_values.values[x] = self.values[x] ** rhs.values[x]
                x += 1
        elif type(rhs) is float: 
            x: int = 0
            while x < len(self.values): 
                simpy_values.values[x] = self.values[x] ** rhs
                x += 1
        return simpy_values

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Determines if Simpy values are equal."""
        final = []
        if type(rhs) is type(self): 
            assert len(self.values) == len(rhs.values)
            x: int = 0
            while x < len(self.values): 
                if self.values[x] == rhs.values[x]: 
                    final.append(True)
                else:
                    final.append(False)
                x += 1
        elif type(rhs) is float:
            x: int = 0
            while x < len(self.values): 
                if self.values[x] == rhs: 
                    final.append(True)
                else: 
                    final.append(False)
                x += 1
        return final
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Determines which Simpy value is greater."""
        final = []
        if type(rhs) is type(self): 
            assert len(self.values) == len(rhs.values)
            x: int = 0
            while x < len(self.values): 
                if self.values[x] > rhs.values[x]: 
                    final.append(True)
                else:
                    final.append(False)
                x += 1
        elif type(rhs) is float:
            x: int = 0
            while x < len(self.values): 
                if self.values[x] > rhs: 
                    final.append(True)
                else: 
                    final.append(False)
                x += 1
        return final
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Gets items from Simpy."""
        if type(rhs) is int: 
            return self.values[rhs]
        else: 
            values = []
            x: int = 0
            while x < len(rhs): 
                if rhs[x]:
                    values.append(self.values[x])
                x += 1
        return Simpy(values)
    # TODO: Your constructor and methods will go here.