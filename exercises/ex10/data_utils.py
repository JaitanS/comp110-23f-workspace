"""Dictionary related utility functions."""

__author__ = "730675117"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Returns file in list of dictionary form."""
    results: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader: 
        results.append(row)
    file_handle.close()
    return results


def column_values(table: list[dict[str, str]], header: str) -> list[str]: 
    """Returns values in a table column under named header."""
    result: list[str] = []
    for row in table:
        result.append(row[header])
    return result


def columnar(table_row: list[dict[str, str]]) -> dict[str, list[str]]: 
    """Makes a table that is organized into a dictionary of columns."""
    table_column: dict[str, list[str]] = {}
    names: dict[str, str] = table_row[0]
    for name in names:
        table_column[name] = column_values(table_row, name)
    return table_column


def head(column_table: dict[str, list[str]], rows: int) -> dict[str, list[str]]: 
    """Creates a table with a set number of rows wanted."""
    results: dict[str, list[str]] = {}
    for column in column_table: 
        row_val: list[str] = []
        if rows >= len(column_table[column]): 
            results[column] = column_table[column]
            continue
        x: int = 0
        while x < rows: 
            row_val.append(column_table[column][x])
            x += 1
        results[column] = row_val
    return results


def select(column_table: dict[str, list[str]], column_select: list[str]) -> dict[str, list[str]]:
    """Creates a table with only the selected columns."""
    results: dict[str, list[str]] = {}
    for name in column_select: 
        results[name] = column_table[name]
    return results


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combines two inputed tables."""
    results: dict[str, list[str]] = {}
    for column in table_1: 
        results[column] = table_1[column]
    for column in table_2: 
        if column in results.keys():
            results[column] += table_2[column]
        else: 
            results[column] = table_2[column]
    return results


def count(val: list[str]) -> dict[str, int]: 
    """Searches for a value in a list and returns the amount of instances."""
    results: dict[str, int] = {}
    for x in val: 
        if x in results.keys(): 
            results[x] += 1
        else: 
            results[x] = 1
    return results