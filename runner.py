import sys
from solutions import *

sol1 = [2756096, 23117829]
sol2 = [572, 612]
sol3 = [196826776, 106780429]
sol4 = [2554, 1916]

# Source: https://github.com/norvig/pytudes/blob/main/ipynb/Advent-2020.ipynb
def do(day: str, *answers: object) -> list[int | None]:
    "E.g., do(3) returns [day3_1(in3), day3_2(in3)]. Verifies `answers` if given."
    g = globals()
    got:  list[int | None] = []
    for part in (1, 2):
        fname = f'day{day}_{part}'
        if fname in g: 
            got.append(g[fname](g[f'in{day}']))
            if len(answers) >= part: 
                assert got[-1] == answers[part - 1], (
                    f'{fname}(in{day}) got {got[-1]}; expected {answers[part - 1]}')
        else:
            got.append(None)
    return got

if __name__ == '__main__':
    day = sys.argv[1]
    g = globals()
    
    sol = g[f'sol{day}'] if f'sol{day}' in g else ()
    result = do(day, *sol)

    print(result)
