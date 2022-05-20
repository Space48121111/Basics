from __future__ import annotations

input = ''' \
  2147483646
'''

'''
output = -42
algorithm/brutal force:
re.compile({x}\d[a-f]) for x in ('+', '-'))
if not [-2^31, 2^31]: ==2^31
'''
def atoi(s: str) -> int:
    max_i, min_i = 2147483647, -2147483648
    # 2**31 - 1, - 2**31
    i, res = 0, 0
    neg = 1
    while i < len(s) and s[i] == ' ':
        i += 1
    if i < len(s) and s[i] == '-':
        neg = -1
        i += 1
    elif i < len(s) and s[i] == '+':
        i += 1

    checker = set('0123456789')
    while i < len(s) and s[i] in checker:
        # floor division
        if (res > max_i // 10 or
        (res == max_i // 10 and ord(s[i]) - ord('0') >= max_i % 10)):
            print('1', res, max_i // 10)
            return max_i if neg == 1 else min_i
        res = res * 10 + int(s[i])
        i += 1
    res = res * neg
    print('2', res)
    # if res < 0:
    #     res = max(res, min_i)
    # res = min(res, max_i)
    #
    return res


print(atoi(input))


# end
