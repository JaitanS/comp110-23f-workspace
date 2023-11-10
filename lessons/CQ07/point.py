"""Practicing with classes."""
from __future__ import annotations
__author__ = "730675117"


class Point: 
    """Coordinate on a graph."""
    x: float
    y: float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
        """Establishes attributes.""" 
        self.x = x_init
        self.y = y_init
    
    def scale_by(self, factor: int) -> None: 
        """Scales and changes point."""
        self.x = self.x * float(factor)
        self.y = self.y * float(factor)
    
    def scale(self, factor: int) -> Point: 
        """Scales and creates new Point."""
        x = self.x * factor
        y = self.y * factor
        return Point(x, y)
    
    def __str__(self) -> str: 
        """Creates readable string for Point."""
        return f"x: {self.x}; y: {self.y}"
    
    def __mul__(self, factor: int | float) -> Point: 
        """Adds multiplication feature."""
        return Point(self.x * factor, self.y * factor)
    
    def __add__(self, num: int | float) -> Point: 
        """Adds addition feature."""
        return Point(self.x + num, self.y + num)