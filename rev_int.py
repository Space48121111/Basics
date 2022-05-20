from __future__ import annotations
import math

input = ''' \
120
'''
'''
output = 21 within signed 32-bit range[-2^31, 2^31 - 1]
otherwise overflows -> 0 out of bounds
-123 -> -321
algorithm/brutal force:
int(reversed(str(s)))
'''
def reverse(x: int) -> int:
    # -2^31, 2^31 - 1
    min, max = -2147483648, 2147483647
    print(min, max)
    res = 0

    while x:
        digit = int(math.fmod(x, 10))
        x = int(x / 10)
        if (res > max // 10 or
        (res == max // 10 and digit >= max % 10)):
            return 0
        if (res < min // 10 or
        (res == min // 10 and digit <= min % 10)):
            return 0
        res = (res * 10) + digit
    return res

print(reverse(-123))

# end
