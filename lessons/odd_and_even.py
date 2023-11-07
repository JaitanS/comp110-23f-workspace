def odd_and_even(x: list[int]) -> list[int]: 
    results: list[int] = []
    for y in range(0, len(x)): 
        if y % 2 == 0: 
            if x[y] % 2 == 1:
                results.append(int(x[y]))
    return results