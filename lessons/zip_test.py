"""Test my zip function."""
__author__ = "730675117"

from lessons.zip import zip


def test_length() -> None: 
    """Tests when lengths of the lists are not the same."""
    test_list1: list[str] = ["cake", "muffin", "cookie"]
    test_list2: list[int] = [1, 2]
    assert zip(test_list1, test_list2) == {}


def test_empty() -> None: 
    """Tests when the lists are empty."""
    test_list1: list[str] = []
    test_list2: list[int] = []
    assert zip(test_list1, test_list2) == {}


def test_dict() -> None: 
    """Tests the normal functionality of zip."""
    test_list1: list[str] = ["cake", "muffin", "cookie"]
    test_list2: list[int] = [1, 2, 3,]
    assert zip(test_list1, test_list2) == {'cake': 1, 'muffin': 2, 'cookie': 3}