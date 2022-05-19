from __future__ import annotations
import fileinput

input = ''' \
FBFBBFFRLR
BFFFBBFRRR

'''
'''
output = 567 357 row 44 * 8(2 to the power of 3) + column 5
output 1 = 358 +1 -1 next
r = [0, 127]
algorithem/brutal force:
for letter in input:
    letter == 'F' or 'L': r = [l: r/2 - 1]
    letter == 'B' or 'R': r = [r/2: r]
div by 2 <=> binary -> int
'''

def binary(s: str) -> int:
    # creating a mapping table
    # replace('F', '0')
    t = str.maketrans('FBLR', '0101')
    # s.strip().splitlines()
    b_s = set(int(l.translate(t), 2) for l in s)
    lo, hi = min(b_s), max(b_s)

    id = next(i for i in range(lo + 1, hi) if i not in b_s)

    return hi, id

input1 = fileinput.input('boarding_ps.txt')
print(binary(input1))






# end
