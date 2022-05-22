from __future__ import annotations

input = ["flower","flow","flight"]

'''
output = 'fl'
algorithm/brutal force:
res = ''
for s in str:
    for l in s:
        if str[s[l]] == str[s + 1][l]:
            res += s[str[l]]
return res
'''

def longest(strs: List[str]) -> str:
    res = ''
    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return res
        res += strs[0][i]
    return res


print(longest(input))









# end
