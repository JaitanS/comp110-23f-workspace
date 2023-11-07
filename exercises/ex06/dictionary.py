"""EX06 - Dictionary funcrions."""
__author__ = "730675117"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Inverts keys and values."""
    result: dict[str, str] = {}
    for x in input: 
        if input[x] in result:
            raise KeyError("KeyError")
        new_key: str = input[x]
        result[new_key] = x
    return result
    

def favorite_color(input: dict[str, str]) -> str: 
    """Returns the most popular color."""
    colors: dict[str, int] = {}
    high_val: int = 0
    high_key: str = ""
    for x in input: 
        if input[x] not in colors: 
            colors[input[x]] = 1
        else: 
            colors[input[x]] += 1
    for x in colors: 
        if colors[x] > high_val: 
            high_val = colors[x]
            high_key = x
    return high_key


def count(input: list[str]) -> dict[str, int]: 
    """Counts the amount of times a value appears."""
    result: dict[str, int] = {}
    for val in input:
        if val not in result: 
            result[val] = 1
        else: 
            result[val] += 1
    return result


def alphabetizer(input: list[str]) -> dict[str, list[str]]: 
    """Catagorizes words by letter."""
    alphabatized: dict[str, list[str]] = {}
    for x in input: 
        if x[0] not in alphabatized:
            alphabatized[x[0]] = [x]
        else: 
            alphabatized[x[0]] += [x]
    return alphabatized


def update_attendance(input: dict[str, list[str]], day: str, name: str) -> dict[str, list[str]]: 
    """Takes a list and mutates it according to attendance."""
    if day in input: 
        input[day] += [name]
    else: 
        input[day] = [name]
    return input