from __future__ import annotations
# import fileinput  # fileinput.input() fileinput.py
from itertools import combinations
from math import prod

input = ''' \
1721
979
366
299
675
1456
'''
'''
ouput = 514579 = 1721 * 299
ouput1 = 241861950 = 979 * 366 * 675
'''

def parsing(s: str) -> set(int): # no dups
    l = [s.strip().splitlines()]
    for i in l:
        n_s = set(i)
    n = set(int(j) for j in n_s)
    return n

def two(s: str) -> int:
    n = parsing(s)
    for x in n:
        if (y := 2020 - x) in n:
            return x * y

def three(s: str) -> int:
    n = parsing(s)
    s = [c for c in n]
    for i, x in enumerate(s):
        yz = 2020 - x
        for y in s[i + 1: ]:
            if (z := yz - y) in n:
                return x * y * z

# print(two(input))
# print(three(input))

# edge cases: 1010 or dups
def solve(s: str, len: int) -> int:
    s = parsing(s)
    n = list(map(int, s))
    for c in combinations(n, len):
        if sum(c) == 2020:
            return prod(c)


print(solve(input, 2))
print(solve(input, 3))



# end
