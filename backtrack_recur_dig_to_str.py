from __future__ import annotations

input = ''' \
23
'''
'''
output = ["ad","ae","af","bd","be","bf","cd","ce","cf"]

algorithm/brutal force:
dict = {2: 'abc'}
for _ in input: res = [l[i] for i in l for l in dict[l].values()]
'''
def backtrack_dig_to_str(digits: str) -> List[str]:
    res = []
    dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', \
    '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    def backtrack(i: int, curr: str) ->List[str]:
        if len(curr) == len(digits):
            res.append(curr)
            return
        for c in dict[digits[i]]:
            backtrack(i + 1, curr + c)
    if digits:
        backtrack(0, '')
    return res

print(backtrack_dig_to_str(input.strip()))





# end
