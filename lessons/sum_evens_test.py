"""Testing my summation Function"""

from sum_evens import sum_evens_list

def test_empty_sum() -> None: 
    """sum_evens of empty list should be 0"""
    assert sum_evens_list([]) == 0

def test_list_length_1(): 
    """Testing on a list with one element"""
    test_list: list[int] = [2]
    assert sum_evens_list(test_list) == 2

def test_list_positives():
    """"""
    test_list: list[int] = [1, 2, 3, 4]
    assert sum_evens_list(test_list) == 6

def test_list_negs_and_pos(): 
    """"""
    test_list: list[int] = [1,-2,3,4]
    assert sum_evens_list(test_list) == 2
