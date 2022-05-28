from __future__ import annotations

n = 3

'''
output = ["((()))","(()())","(())()","()(())","()()()"]
algorithm/brutal force:
# hashmap = {'(': ')'}
def generator_parens(n):
    def backtrack(open, close): if == n: res.app(''.join(st) ret
    if o < n: st.app() bt(o + 1, cl) st.pop()
    if cl < o:  bt(c, cl + 1)
'''

def generator_parens(n: int) -> List[str]:
    res = []
    stack = []
    def bt(o: str, c: str) -> List[str]:
        if o == c == n:
            res.append(''.join(stack))
            return
        if o < n:
            stack.append('(')
            # increm count
            bt(o + 1, c)
            # update global var, not pass to every call
            stack.pop()
        if c < o:
            stack.append(')')
            bt(o, c + 1)
            stack.pop()
    bt(0, 0)
    return res


print(generator_parens(n))




# end
