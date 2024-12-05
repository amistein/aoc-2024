import re

from .data import get_data

in3 = get_data(3)

day3_operation_regex = r'mul\([0-9]{1,3},[0-9]{1,3}\)'
day3_operand_regex = r'mul\(([0-9]{1,3}),([0-9]{1,3})\)'

def day3_1(memory: str):
    operands = re.findall(day3_operand_regex, memory)
    
    return sum([int(a) * int(b) for a, b in operands])

def day3_2(memory: str):
    activated = True
    all_operands: list[tuple[str, str]] = []
    i = 0

    while i < len(memory):
        re_match = re.match(day3_operation_regex, memory[i:i+12])
        if re_match and activated:
            operation = re_match.group(0)
            operands = re.match(day3_operand_regex, operation).groups()

            all_operands.append(operands)
            i += len(operation)
        elif memory[i:i + 4] == 'do()':
            activated = True
            i += 4
        elif memory[i:i + 7] == "don't()":
            activated = False
            i += 7
        else:
            i += 1

    return sum([int(a) * int(b) for a, b in all_operands])
