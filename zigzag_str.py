from __future__ import annotations

input = ''' \
PAYPALISHIRING
'''
'''
output = 'PAHNAPLSIIGYIR' numRows = 3
P   A   H   N
A P L S I I G
Y   I   R

output - 'PINALSIGYAHRPI' numRows = 4
P     I    N
A   L S  I G
Y A   H R
P     I

algorithm/brutal force:
for i in len(range(input)):
    # row[r % (numRows - 1)]
    row[0]col[c++]
    row[1]col[numRows - 1]
    row[2]col[numRows - 2]
    row[numRows - 1]col[c++]
    for r c in pos[row][col]

'''

def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s

    res = ''
    for r in range(numRows):
        incre = 2 * (numRows - 1)
        # i: pointer in the res
        # start with index 0 for row 0, index 1 for row 1
        for i in range(r, len(s), incre):
            res += s[i]
            if (r > 0 and r < numRows - 1 and
            (i + incre - 2 * r) < len(s)):
                res += s[i + incre - 2 * r]
    return res


print(convert(input.strip(), 4))


# end
