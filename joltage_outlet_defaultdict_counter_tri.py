from collections import defaultdict
from functools import cache

input = ''' \
16
10
15
5
1
11
7
19
6
12
4
'''

'''
output = 35 7 * 5 for 1 jolt and 3 jolts 3 diff
output1 = 8 arrangements/combinations
algorithm/brutal force:
spl() ls = [] i in [1, 2, 3] sort
while ls[n] <= m = max() + 3 diff = ls[n] - ls[n - 1] if d == 1 ct += 1 3
ls[n + 1] = ls[n + i] ct += 1
tribonacci fibonacci
'''

def tri(s):
    ad = [0] + sorted(map(int, s.splitlines()))
    ad.append(ad[-1] + 3)
    diff = defaultdict(int)
    ct = defaultdict(int, {0:1})
    for a, b in zip(ad[1:], ad):
        diff[a - b] += 1
        ct[a] = ct[a - 3] + ct[a - 2] + ct[a - 1]
    return (diff[3] * diff[1]), ct[ad[-1]]

input1 = open('joltage_outlet.txt', 'r').read()
print(tri(input))

def c(s):
    ct = Counter({3:1})
    s_i = sorted(int(l) for l in s.splitlines())
    p1 = 0
    for i in s_i:
        ct[i - n] += 1
        p1 = i
    return ct[3] * ct[1]

@cache
def streak(n):
    assert n >= 2
    if n == 2:
        return 1
    elif n == 3:
        return 2
    elif n == 4:
        return 4
    else:
        return streak(n - 3) + streak(n - 2) + streak(n - 1)

def c_v(s):
    comb = streak = 1
    prev = 0
    for n1 in s:
        if n1 == p + 1:
            streak += 1
        elif streak > 1:
            comb *= streak(streak)
            streak = 1
            prev = n1

    return comb









# end
