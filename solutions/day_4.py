from .data import get_data, parse

data = get_data(4)
in4 = parse(data)

day_4_1_word = 'XMAS'
day_4_2_word = 'MAS'

def day4_1(input: list[str]) -> int:
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    res = 0
    
    for row in range(len(input)):
        for col in range(len(input[row])):
            res += sum([search(input, day_4_1_word, 0, row, col, dir) for dir in dirs])

    return res

def day4_2(input: list[str]):
    res = 0

    for row in range(len(input)):
        for col in range(len(input[row])):
            if search(input, day_4_2_word, 0, row, col, (1, 1)) and \
                (search(input, day_4_2_word, 0, row, col + 2, (1, -1)) or search(input, day_4_2_word, 0, row + 2, col, (-1, 1))):
                    res += 1
            if search(input, day_4_2_word, 0, row, col, (-1, -1)) and \
                (search(input, day_4_2_word, 0, row, col - 2, (-1, 1)) or search(input, day_4_2_word, 0, row - 2, col, (1, -1))):
                    res += 1

    return res

def search(input: list[str], word: str, idx: int, row: int, col: int, next_move: tuple[int, int]) -> int:
    if idx == len(word):
        return 1
    if row < 0 or row >= len(input) or col < 0 or col >= len(input[row]) or input[row][col] != word[idx]:
        return 0
    
    row_inc, col_inc = next_move
    return search(input, word, idx + 1, row + row_inc, col + col_inc, next_move)
