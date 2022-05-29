from __future__ import annotations
import re
from typing import Match

input = ''' \
5 + (8 * 3 + 9 + 3 * 4 * 3)
'''

'''
output = 437 left-to-right
output1 = 1445 addition in precedence of multiplication
algorithm/brutal force:
parens, add = re.compile(\d+ \( \+)
def replace_add/add_sub_callback(match) match[1] + match[2]
def compute_val: w add.search s = a.sub(a_c, s) val = ps[0] w op = [i] n = [i + 1]
if '(': [] op: if '+': val += n if '*':
def parens_sub_callback/replace: str(c_v(match[1])
def compute() : f l: w p.search(l: p.sub(p_c, ps): to += c_v(l)
'''

class I(int):
    def __add__(a, b):
        return I(a.real + b.real)
    def __sub__(a, b):
        return I(a.real * b.real)
    __mul__ = __add__

def comp(s):
    ls = re.sub(r'(\d+)', r'I(\1)', s).replace('*', '-').splitlines()
    return sum(eval(l) for l in ls), \
    sum(eval(l.replace('+', '*')) for l in ls)
    # replace + with * to have the same precedence

# print(comp(input))

class Operation:
    p = re.compile(r'\(([^()]+)\)')
    add = re.compile(r'(\d+) \+ (\d+)')
    def rep_a(self, m: Match[str]) -> str:
        return str(int(m[1]) + int(m[2]))
    def c_v(self, s: str) -> int:
        print(f'==> {s}')
        while self.add.search(s):
            s = self.add.sub(self.rep_a, s)
        ps = s.split()
        val = int(ps[0])
        i = 1
        while i < len(ps):
            op = ps[i]
            n = int(ps[i + 1])
            if op == '*':
                val *= n
            elif op == '+':
                val += n
            else:
                raise AssertionError(val, op, n)
            i += 2
        return val
    def p_rep(self, m: Match[str]) -> str:
        return str(self.c_v(m[1]))
    def c(self, s: str) -> int:
        to = 0
        for l in s.splitlines():
            while self.p.search(l):
                l = self.p.sub(self.p_rep, l)
            to += self.c_v(l)
        return to

input1 = open('op_order.txt', 'r').read()
o = Operation()
print(o.c(input))








# end
