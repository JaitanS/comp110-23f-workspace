
"""List functions."""
__author__ = 730675117


def all(input: list[int], input2: int) -> bool:
    """Evaluates whether a list contains all the given numbers."""
    int_eval: int = 0
    same_int: int = 0
    if len(input) < 1: 
        return False
    while int_eval < len(input):
        if input[int_eval] == input2:
            same_int += 1
            int_eval += 1
        else: 
            int_eval += 1
    if same_int == len(input):
        return True
    return False


def max(input: list[int]) -> int: 
    """Given a list of ints, returns the highest."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    int_eval: int = 0
    high_int: int = int(input[0])
    while int_eval < (len(input)):
        if high_int < input[int_eval]: 
            high_int = input[int_eval]
            int_eval += 1
        else: 
            int_eval += 1
    return high_int


def is_equal(input: list[int], input2: list[int]) -> bool: 
    """Checks to see if inputes lists are equal."""
    if len(input) != len(input2):
        return False
    int_eval: int = 0
    same_int: int = 0
    while int_eval < len(input):
        if input[int_eval] == input2[int_eval]:
            same_int += 1
            int_eval += 1
        else: 
            int_eval += 1
    if same_int == len(input): 
        return True
    else: 
        return False