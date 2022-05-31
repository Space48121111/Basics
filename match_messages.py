import regex

input = ''' \
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb
'''

input1 = ''' \
42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba
'''
'''
output = 2 ababbb and abbbab match rule 0 definite
8: 42 => 8: 42 | 42 8
11: 42 31 => 11: 42 31 | 42 11 31
output1 = 3 12
update/replace/adjust w/h '8' n '11' +loop/cycles infinite valid

algorithm/brutal force:
parse: raw_rules, messages = sp('\n\n') t = sp(': ') splitlines()
def expand(v) if not v.isdig(): return v
while t: {t: s} seen [0] if t == r: line[t] res.append(r)
def solve(): ret re.fm(s.sp())
'''
class rules:
    def __init__(self):
        pass
    def so(self, rs, me):
        def exp(v):
            if not v.isdigit():
                return v
            return '(?:' + ''.join(map(exp, rs[v].split())) + ')'
        res = regex.compile(exp('0'))
        return sum(res.fullmatch(m) is not None for m in me)

    def parse(self, s):
        r_r, me = s.strip().split('\n\n')
        me = me.splitlines()
        rs = dict(r.strip().replace('"', '').split(':', 1) for r in r_r.splitlines())
        # print(rs) # (?:(?:b)(?:a)|(?:b)(?:b)))
        return rs, me
    def new_r(self, rs):
        rs['8'] = '42 +'
        rs['11'] = '(?P<R> 42 (?&R)? 31 )'
        # print(rs) # dict
        return rs

r = rules()
rs, me = r.parse(input1)
print(r.so(rs, me))
n_rs = r.new_r(rs)
# print(n_rs, me)
print(r.so(n_rs, me))


class dict:
    def c(s):
        rs = {}
        for l in r_r.splitlines():
            k, _, v = l.partition(': ')
            rs[k] = v
        def _get_re(s):
            if s == ' | ':
                return s
            rs = rs[s]
            if rs.startswith('"'):
                return rs.strip('"')
            else:
                return f ''({'.join(_get_re(p) for p in rs.split())})'
        res = re.compile(_get_re('0'))
        return sum(bool(res.fullmatch(m) for m in me.splitlines()))

        re_42 = re.compile(_get_re('42'))
        re_31 = re.compile(_get_re('31'))
        ct = 0
        for m in me.splitlines():
            p = 0
            ct_42 = 0
            while match := re_42.Match(m, p):
                ct_42 += 1
                pos = match.end()

            # 31 repeat the above 42
            if 0 < ct_31 < ct_42 and p == len(m):
                ct += 1
    print(ct)
# dict algorithm only, I degress...





# end
