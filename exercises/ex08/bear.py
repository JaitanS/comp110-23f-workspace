"""File to define Bear class."""


class Bear:
    """Class to define Bear."""
    age: int
    hunger_score: int

    def __init__(self) -> None:
        """Gives values to attributes."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self) -> None:
        """Increase age by 1."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int) -> None: 
        """Models a bear eating fish."""
        self.hunger_score += num_fish