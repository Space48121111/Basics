import re

input = ''' \
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12

'''
'''
output = 71 4 + 55 + 12 invalid
output1 =
algorithm/brutal force:
rules, t, neighbor = split('\n\n') lo, hi = rules.splitlines().split(' or ')
for n in nei.spl(): if not in [lo:hi]: ret v = n
for v in nei.spl().split(','):
    if in cl[lo:hi]:
        if in row[lo:hi]:
            a = seat
        else: if in seat[lo:hi]: a = row
    else: a = cl

'''

def indices_matrix(s):
    rules = []
    r_r, y_t, ne = s.strip().split('\n\n')
    re_s = re.compile(r'([^:]+): (\d+)-(\d+) or (\d+)-(\d+)')
    for line in r_r.splitlines():
        (field, lo1, hi1, lo2, hi2) = re_s.fullmatch(line).groups()
        rules.append((field, int(lo1), int(hi1), int(lo2), int(hi2)))
    cols = [set(range(len(rules))) for _ in range(len(rules))]
    print(cols)
    error = 0
    for ti in ne.splitlines()[1:]:
        valid = True
        t_r = []
        for n in map(int, ti.split(',')):
            match = set(i for i, (_, lo1, hi1, lo2, hi2) in enumerate(rules) \
            if lo1 <= n <= hi1 or lo2 <= n <= hi2)
            if not match:
                valid = False
                error += n
            elif valid:
                t_r.append(match)
        if valid:
            for col, m in zip(cols, t_r):
                col &= m
    print(error)

    to = 1
    singles = set()
    y_t = list(map(int, y_t.splitlines()[-1].split(',')))
    while len(singles) != len(rules):
        for i, col in enumerate(cols):
            if len(col) > 1:
                col -= singles
            elif len(col) == 1:
                singles |= col
                if rules[col.pop()][0].startswith('Departure'):
                    to *= y_t[i]
    print(to)

indices_matrix(input)





# end
