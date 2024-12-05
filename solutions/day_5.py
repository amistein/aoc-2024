from collections import defaultdict

from .data import get_data, parse, paragraphs
from .parsers import ints

data = get_data(5)
raw_rules, raw_updates = parse(data, sections=paragraphs)
rules = parse(raw_rules, ints)
updates = parse(raw_updates, ints)
in5 = [rules, updates]

def day5_1(input: list[list[list[int]]]):
    rules, updates = input
    res, _ = update_sums(rules, updates)
    
    return res

def day5_2(input: list[list[list[int]]]):
    rules, updates = input
    _, res = update_sums(rules, updates)
    
    return res

def update_sums(rules: list[list[int]], updates: list[list[int]]):
    rule_table: defaultdict[int, list[int]] = defaultdict(list)
    correct_sum = incorrect_sum = 0
    
    for page1, page2 in rules:
        rule_table[page1].append(page2)

    for update in updates:
        correct_update = topo_sort(rule_table, set(update))
        mid = len(update) // 2
        val = correct_update[mid]
        
        if  correct_update == update:
            correct_sum += val
        else:
            incorrect_sum += val

    return (correct_sum, incorrect_sum)

def topo_sort(rules: defaultdict[int, list[int]], page_set: set[int]):
    res: list[int] = []
    visited: set[int] = set()

    for page in page_set:
        dfs(page, rules, page_set, visited, res)
    
    return res[::-1]

def dfs(page: int, rules: defaultdict[int, list[int]], page_set: set[int], visited: set[int], res: list[int]):
    if page in visited or page not in page_set:
        return
    
    visited.add(page)
    
    for next_page in rules[page]:
        dfs(next_page, rules, page_set, visited, res)

    res.append(page)