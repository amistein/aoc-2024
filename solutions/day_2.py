from .data import get_data
from .utils import ints

in2 = get_data(2, ints)

def day2_1(records: list[list[int]]):
    return len([record for record in records if is_safe(record)])

def day2_2(records: list[list[int]]):
    return len([record for record in records if is_safe_by_removing(record)])

def is_safe(record: list[int]):
    is_increasing = record[0] < record[1]
    if is_increasing:
        return all([is_valid_diff(record[i], record[i - 1]) for i in range(1, len(record))])
    else:
        return all([is_valid_diff(record[i - 1], record[i]) for i in range(1, len(record))])

def is_valid_diff(a: int, b: int):
    return a - b > 0 and a - b <= 3

def is_safe_by_removing(record: list[int]):
    return any([is_safe(record[:i] + record[i + 1:]) for i in range(len(record))])
