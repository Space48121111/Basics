input = ''' \
abcabcbb
'''

'''
output = 3 'abc'
bbbbb -> 1 b
pwwkew ->3 wke
constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

algorithm: contiguous -> sliding window
Time complexity: O(n)
Space complexity: O(n)

'''

def contiguous(s: str) -> int:
    l = 0
    bucket = set()
    max_s = 0

    for r in range(len(s)):
        while s[r] in bucket:
            bucket.remove(s[l])
            l += 1
        bucket.add(s[r])
        max_s = max(max_s, r - l + 1)
    return max_s

print(contiguous(input))









# end
