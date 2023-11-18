"""File to define River class."""

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear

__author__ = "730675117"


class River:
    """Defines a river class."""
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int) -> None:
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self) -> None:
        """Checks ages."""
        fish_left: list[Fish] = []
        for fish in self.fish: 
            if fish.age <= 3: 
                fish_left.append(fish)
        self.fish = fish_left
        bears_left: list[Bear] = []
        for bear in self.bears: 
            if bear.age <= 5: 
                bears_left.append(bear)
        self.bears = bears_left
        return None

    def bears_eating(self) -> None:
        """Models a bear eating."""
        for bear in self.bears: 
            if len(self.fish) > 4: 
                self.remove_fish(3)
                bear.eat(3)
        return None
    
    def check_hunger(self) -> None:
        """Checks hunger of bears."""
        bear_left: list[Bear] = []
        for bear in self.bears: 
            if bear.hunger_score >= 0: 
                bear_left.append(Bear)
        self.bears = bear_left
        return None
        
    def repopulate_fish(self) -> None:
        """Repopulates fish in river."""
        mates: int = len(4 * self.fish) // 2
        x: int = 0
        while x < mates: 
            self.fish.append(Fish())
        return None
    
    def repopulate_bears(self) -> None:
        """Repopulates bears in river."""
        mates: int = len(self.bears) // 2
        x: int = 0
        while x < mates: 
            self.bears.append(Bear())
        return None

    def remove_fish(self, amount: int) -> None: 
        """Removes fish."""
        x: int = 0
        while x < amount:
            self.fish.pop(0)
            x += 1
        return

    def view_river(self) -> None:
        """Prints river stats."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return

    def one_river_day(self) -> None:
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
    
    def one_river_week(self) -> None: 
        """Calls one_river_day seven times."""
        x = 1 
        while x < 8:
            self.one_river_day()
            x += 1
        return None