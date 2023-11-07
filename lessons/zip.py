"""Combining two lists into a dictionary."""
__author__ = "730675117"


def zip(input1: list[str], input2: list[int]) -> dict[str, int]: 
    """Combines two lists into a single dictionary."""
    result: dict[str, int] = {}
    if len(input1) == 0 or len(input2) == 0: 
        return {}
    if len(input1) != len(input2): 
        return result
    i: int = 0
    while i < len(input1): 
        result[input1[i]] = input2[i]
        i += 1
    return result
