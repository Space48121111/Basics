from collections import deque

input = ''' \
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
'''
'''
output = 127 15-40
output1 = 62 15 + 47 smallest + largest
'''

def compute(s, a):
    n = [int(x) for x in s.splitlines()]
    preamble = deque(n[:a])
    invalid = None
    for i in n[a:]:
        seen = set()
        for j in preamble:
            if i - j in seen:
                preamble.popleft()
                preamble.append(i)
                # print(preamble)
                break
            seen.add(j)
            # print(seen)
        else:
            invalid = i
            break
    print(invalid)
    start = end = total = 0
    while total != invalid:
        while total < invalid:
            total += n[end]
            end += 1
        while total > invalid:
            total -= n[start]
            start += 1
    print(min(n[start:end]) + max(n[start:end]))

def compute1(s: str) -> int:
    for i in range(n, len(s)): # x, y, n, i
        prev = s[i - n:i]
        for x, y in itertools.combinations(prev, 2):
            if s[i] == x + y:
                break
            else:
                inv = s[i]
                return inv
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            a = s[i, j + 1]
            if sum(a) == inv:
                return min(a) + max(a)


input1 = open('preamble_deque.txt', 'r').read()
compute(input1, 25)







# end
