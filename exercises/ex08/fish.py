"""File to define Fish class."""


class Fish:
    """Defines a fish class."""
    age: int

    def __init__(self) -> None:
        """Gives values to attributes."""
        self.age = 0
        return None
    
    def one_day(self) -> None:
        """Increase age by 1."""
        self.age += 1
        return None