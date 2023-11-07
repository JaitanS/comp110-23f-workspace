"""Practicing with classes."""
from __future__ import annotations
__author__ = "730675117"


class Point: 
    """Coordinate on a graph."""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
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
    