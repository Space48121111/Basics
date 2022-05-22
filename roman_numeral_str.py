input = ''' \
58
'''
'''
ouput = LVIII
inp1 = 1994
output1 = MCMXCIV
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
algorithm/brutal force:
res = ''
dict = {val: symbol} singles, fives, tens
for _ in range(len(x)) and x > 0:
    stack = [zeros, tens, thousands= x // 10, x // 100, x // 1000]
    for n in x: n // 10
    while stack:
        n = stack.pop()
        if zeros(n) > 5:
            res.append(fives[n])
            res.append(dict[n - 5])
        if zeros(n) == 4 or 9:
            res.append(dict[singles[1]])
            res.append(dict[n + 1])
        res.append(dict[curr])

'''

def intToRoman(num: int) -> str:
    ls = [['I', 1], ['IV', 4], ['V', 5], ['IX', 9], ['X', 10], ['XL', 40], ['L', 50],
    ['XC', 90], ['C', 100], ['CD', 400], ['D', 500], ['CM', 900], ['M', 1000]]

    res = ''
    for symb, val in reversed(ls):
        if num // val:
            ct = num // val
            res += (symb * ct)
            num = num % val
    return res



print(intToRoman(1994))







# end
