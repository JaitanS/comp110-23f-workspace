"""Summing the elements of a list using different loops."""
__author__ = "730675117"


def w_sum(vals: list[float]) -> float: 
    """Sums variables using while loop."""
    idx: int = 0
    sum: float = 0.0
    while idx < len(vals): 
        sum += vals[idx]
        idx += 1
    return sum


def f_sum(vals: list[float]) -> float: 
    """Sums variables using for loop."""
    sum: float = 0.0
    for num in vals: 
        sum += num
    return sum


def f_range_sum(vals: list[float]) -> float: 
    """Sums list using range."""
    sum: float = 0.0 
    for idx in range(0, len(vals)): 
        sum += vals[idx]
    return sum