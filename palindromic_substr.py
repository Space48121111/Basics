from __future__ import annotations

input = ''' \
babad
'''
'''
output = 'bab' 'aba'
longest palindromic substring 'dabab'
algorithm/ brutal force:
ps = s[i: i + n] each char O(n + n^2)
if ps in s:
    max(len(ps))
'''

def palindromic(s: str) -> str:
    res = ''
    res_len = 0
    for i in range(len(s)):
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > res_len:
                res = s[l: r + 1]
                res_len = r - l + 1
            r += 1
            l -= 1
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > res_len:
                res = s[l: r + 1]
                res_len = r - l + 1
            r += 1
            l -= 1
    print(res_len)
    return res


print(palindromic(input.strip()))






# end
