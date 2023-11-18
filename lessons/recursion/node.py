"""Node Class."""

from __future__ import annotations


__author__ = "730675117"


class Node:
    """My Node class for linked lists."""
    
    data: int
    next: Node | None
    
    def __init__(self, data: int, next: Node | None):
        """Construct Node."""
        self.data = data
        self.next = next
        
    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            # base case (where it ends!)
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"
        
    def head(self) -> int:
        """Part 0."""
        return int(self.data)
    
    def tail(self) -> Node | None:
        """Part 1."""
        return self.next
    
    def last(self) -> int:
        """Part 2."""
        if self.next is None: 
            return self.data
        if self.next.next is None: 
            return self.next.data
        if self.next.next.next is None: 
            return self.next.next.data
        return int(0)