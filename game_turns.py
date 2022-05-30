from __future__ import annotations
from array import array
from collections import defaultdict

input = ''' \
0,3,6
'''
input1 = ''' \
6,19,0,5,7,13,1
'''
'''
output = 436 2020th output1 = 175594 30000000th

algorithm/brutal force:
1. f i, v in enumerate() i = nums[val] last = nu[-1]
prev age = array age[last]
2. prev = {i: n} if n - 1 not in h: n = 0
else: n = i - 1 - (j for n[j] in h) i += 1 h.append((i, n))
'''

def array(s: str) -> int:
    nu = [int(i) for i in s.split(',')]
    l = nu[-1]
    si = 30_000_000
    a = [0] * si
    for i, val in enumerate(nu):
        a[val] = i + 1
    for i in range(len(nu), si):
        if i == 2020:
            print(l)
        p = a[l]
        a[l], l = i, i - p if p else 0
    print(l)

def turn(s: str, n: int) -> int:
    nu = [int(i) for i in s.split(',')]
    p = defaultdict(list)
    # defaultdict(lambda: deque(maxlen = 2))
    # less space yet slower performance 
    for t in range(n):
        if t < len(nu):
            n = nu[t]
        elif len(p[n]) == 1:
            n = 0
        else:
            n = p[n][-1] - p[n][-2]

        p[n].append(t)
    return n

print(array(input1))
# print(turn(input, 2020))
# print(turn(input, 30000000))







# end
