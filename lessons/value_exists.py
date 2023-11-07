def value_exists(x: dict[str, int], y: int) -> bool:
    for z in x: 
        if x[z] == y: 
            return True
    else: 
        return False