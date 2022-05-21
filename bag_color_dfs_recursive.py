from collections import defaultdict, deque
from functools import cache
import re
import fileinput

input = ''' \
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
'''
'''
output = 4 contains at least one shiny gold bag
bright white, muted yellow, dark orange, light red bag
output1 = 32 1 + 1*7 + 2 + 2*11
1 dark olive, 7 bags within it, 2 vibrant plum, 11 within it
algorithm/brutal force:
res = []
for 'shiny gold' in str:
    re.compile(r'[\da-z]{bag}')
    res.append(a-z)
    while True:
        if 'a-z' in str:
            re.compile(r'[\da-z]{bag}')
            res.append(a-z)
return res
'''
# def parse1():
# bags_within
b_w = defaultdict(set)
# bags_contain
b_c = defaultdict(dict)
for line in fileinput.input('bag_color_dfs_recursive.txt'):
# for line in input.strip().splitlines():
    p_s, ch_s = line.split(' bags contain ')
    for ct, ch in re.findall(r'(\d+) (\w+ \w+) bags?[,.]', ch_s):
        b_w[ch].add(p_s)
        b_c[p_s][ch] = int(ct)
@cache
def w(n):
    ls = b_w[n].copy()
    for b in b_w[n]:
        ls.update(w(b))
    return ls
@cache
def c(n):
    return sum(ct + ct * c(b) for b, ct in b_c[n].items())
def s_w(n):
    cls, ps = deque([n]), set()
    while cls:
        for p in b_w[cls.pop()]:
            if p not in ps:
                ps.add(p)
                cls.appendleft(p)
    return len(ps)
def s_c(n):
    cls, t = deque([(n, 1)]), -1
    while cls:
        cl, m = cls.pop()
        t += m
        for ch, ct in b_c[cl].items():
            cls.appendleft((ch, ct * m))
    return t


print(len(w('shiny gold')))
print(c('shiny gold'))
print(s_w('shiny gold'))
print(s_c('shiny gold'))


# def parse2()



# end
