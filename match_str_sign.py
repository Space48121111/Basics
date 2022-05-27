from __future__ import annotations

input = ''' \
()[]{}
'''
'''
output = True
algorithm/brutal force:
dict = {'(': ')'}
for i in s: for j in s[-1:]: if dict[i] == j: ret T
re.match()
remove -> pop stack ) -> (
'''

def validity(s: str) -> bool:
    stack = []
    hashmap = {')': '(', '}': '{', ']': '['}
    # building the stack
    for c in s:
        # print(c)
        if c in hashmap:
            if stack and stack[-1] == hashmap[c]:
                # print(stack)
                stack.pop()
            else:
                return False
        else:
            stack.append(c)

    return True if not stack else False

print(validity(input.strip()))





# end
