from collections import Counter

from .data import get_data, parse
from .parsers import int_pair

data = get_data(1)
in1 = parse(data, int_pair)

def day1_1(pairs: list[tuple[int, int]]):
    sorted_list1 = sorted(get_list1(pairs))
    sorted_list2 = sorted(get_list2(pairs))

    return sum([abs(a - b) for a, b in zip(sorted_list1, sorted_list2)])

def day1_2(pairs: list[tuple[int, int]]):
    list1 = get_list1(pairs)
    list2 = get_list2(pairs)
    counter = Counter(list2)

    return sum([n * counter.get(n, 0) for n in list1])

def get_list1(pairs: list[tuple[int, int]]):
    return [e for e, _ in pairs]

def get_list2(pairs: list[tuple[int, int]]):
    return [e for _, e in pairs]