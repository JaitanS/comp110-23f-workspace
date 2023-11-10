"""Tests funstionality of dict functions."""
__author__ = "730675117"


from dictionary import invert
from dictionary import favorite_color
from dictionary import count
from dictionary import alphabetizer
from dictionary import update_attendance


def test_invert_letters() -> None: 
    """Tests the normal functionality of invert with letters."""
    test_dict1: dict[str, str] = {"A": "a", "B": "b", "C": "c"}
    assert invert(test_dict1) == {"a": "A", "b": "B", "c": "C"}


def test_invert_empty() -> None:
    """Tests the resulting dictionary length."""
    test_dict1: dict[str, str] = {}
    assert invert(test_dict1) == {}


def test_invert_numbers() -> None: 
    """Tests the normal functionality of invert funcrion with numbers."""
    test_dict1: dict[str, str] = {"1": "2", "3": "4", "5": "6"}
    assert invert(test_dict1) == {"2": "1", "4": "3", "6": "5"}


def test_color_allred() -> None:
    """Tests functionality of favorite_color when the colors are all the same."""
    test_dict1: dict[str, str] = {"Marc": "Red", "Tom": "Red", "Sarah": "Red"}
    assert favorite_color(test_dict1) == "Red"


def test_color_norm() -> None: 
    """Tests functionality of favorite_colors with an expected dictionary."""
    test_dict1: dict[str, str] = {"Marc": "Red", "Tom": "Purple", "Sarah": "Blue", "Tommy": "Purple"}
    assert favorite_color(test_dict1) == "Purple"


def test_color_empty() -> None: 
    """Tests favorite_colors when dict is empty."""
    test_dict1: dict[str, str] = {}
    assert favorite_color(test_dict1) == ""


def test_count_numbers() -> None: 
    """Tests functionality of count function with expected list of numbers."""
    test_list1: list[str] = ["1", "2", "3", "1", "2", "1"]
    assert count(test_list1) == {"1": 3, "2": 2, "3": 1}


def test_count_empty() -> None: 
    """Tests count when input list is empty."""
    test_list1: list[str] = []
    assert count(test_list1) == {}


def test_count_words() -> None: 
    """Tests functionality of count function with words."""
    test_list1: list[str] = ["Egor", "Jaitan", "Gordan", "Egor", "Egor"]
    assert count(test_list1) == {"Egor": 3, "Jaitan": 1, "Gordan": 1}


def test_alphabetizer_names() -> None: 
    """Tests functionality of alphabetizer using names."""
    test_list1: list[str] = ["Egor", "Elizabeth", "Jaitan", "James", "Gordan"]
    assert alphabetizer(test_list1) == {"E": ["Egor", "Elizabeth"], "J": ["Jaitan", "James"], "G": ["Gordan"]}


def test_alphabetizer_animals() -> None:
    """Tests functionality of alphabetizer using animals."""
    test_list1: list[str] = ["Lion", "Lizard", "Cat", "Turtle", "Tiger"]
    assert alphabetizer(test_list1) == {"L": ["Lion", "Lizard"], "C": ["Cat"], "T": ["Turtle", "Tiger"]}


def test_alphabetizer_empty() -> None: 
    """Tests alphabetizer function when given an empty list."""
    test_list1: list[str] = []
    assert alphabetizer(test_list1) == {}


def test_attendance_day() -> None: 
    """Tests update_attendance function when given expected day as name."""
    test_dict1: dict[str, list[str]] = {"Monday": ["Sarah", "Tommy"], "Tuesday": ["Tommy", "Chris"], "Wednesday": ["Chris", "Tommy", "Sarah"]}
    test_day: str = "Tuesday"
    test_name: str = "Sarah"
    assert update_attendance(test_dict1, test_day, test_name) == {"Monday": ["Sarah", "Tommy"], "Tuesday": ["Tommy", "Chris", "Sarah"], "Wednesday": ["Chris", "Tommy", "Sarah"]}


def test_attendance_new() -> None: 
    """Tests update_attendance when there is a new key given to update."""
    test_dict1: dict[str, list[str]] = {"Monday": ["Sarah", "Tommy"], "Tuesday": ["Tommy", "Chris"], "Wednesday": ["Chris", "Tommy", "Sarah"]}
    test_day: str = "Thursday"
    test_name: str = "Sarah"
    assert update_attendance(test_dict1, test_day, test_name) == {"Monday": ["Sarah", "Tommy"], "Tuesday": ["Tommy", "Chris"], "Wednesday": ["Chris", "Tommy", "Sarah"], "Thursday": ["Sarah"]}


def test_attendace_num() -> None: 
    """Tests update_attendance functionality when given date as a number."""
    test_dict1: dict[str, list[str]] = {"4/3/2023": ["Sarah", "Tommy"], "4/4/2023": ["Tommy", "Chris"], "4/5/2023": ["Chris", "Tommy", "Sarah"]}
    test_day: str = "4/4/2023"
    test_name: str = "Sarah"
    assert update_attendance(test_dict1, test_day, test_name) == {"4/3/2023": ["Sarah", "Tommy"], "4/4/2023": ["Tommy", "Chris", "Sarah"], "4/5/2023": ["Chris", "Tommy", "Sarah"]}