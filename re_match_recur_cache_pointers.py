from __future__ import annotations

input = ''' \
s = 'aa', p = '.*'
'''

'''
output = True
for j in p:
    for i in s:
        if j == i or j = '.' and len(s) == len(p):
            return True
        elif j = '*' and i in [a-z]:
            while True: recursive
                j+=1

'''

def isMatch(s: str, p:str) -> bool:
    cache = {}
    def dfs(i:int, j: int) -> bool:
        if (i, j) in cache: # key error
            return cache[(i, j)]
        if i >= len(s) and j >= len(p):
            return True
        if j >= len(p):
            return False
        match = i < len(s) and (s[i] == p[j] or p[j] == '.')
        if (j + 1) < len(p) and p[j + 1] == '*':
            cache[(i, j)] = dfs(i, j + 2) or (match and dfs(i + 1, j))
            # print((s[i], p[j]))
            return cache[(i, j)]
        if match:
            cache[(i, j)] = dfs(i + 1, j + 1)
            return cache[(i, j)]
        cache[i, j] = False
        return False
    return dfs(0, 0)


print(isMatch('aab', 'c*a*b'))






# end
