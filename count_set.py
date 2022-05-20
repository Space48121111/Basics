from __future__ import annotations

input = ''' \
abc

a
b
c

ab
ac

a
a
a
a

b
'''
'''
output = 11 union
output1 = 6 intersection agreed-upon
algorithm/brutal force:
yes = set()
sss = s.split('\n\n')
for _ in sss:
    ss = sss.strip('\n')
for i in len(ss):
    if not in yes: yes.add(i)
ret len(yes)
'''
def expr(s: str) -> int:
    t1 = t2 = 0
    for group_s in s.split('\n\n'):
        t1 += len(set(group_s.replace('\n', '')))
        t2 += len(set.intersection(*map(set, group_s.split())))
    return t1, t2

def parse(s: str) -> List[List[set[str]]]:
    global res
    res = []
    for group_s in s.split('\n\n'):
        g = []
        for user_s in group_s.strip().splitlines():
            g.append(set(user_s))
        res.append(g)
    return res
def compute() -> int:
    global res
    t = 0
    for group in res:
        accum = set()
        for user in group:
            accum |= user
        t += len(accum)
    return t
def compute1() -> int:
    global res
    t = 0
    for group in res:
        accum = group[0]
        for user in group:
            accum &= user
        t += len(accum)
    return t

def compute0(s: str) -> int:
    t = 0
    for group_s in s.split('\n\n'):
        t += len(set(group_s) - {'\n'})
    return t



# print(expr(input))
# print(compute0(input))
print(parse(input))
print(compute1())





# end
