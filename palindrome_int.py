input = ''' \
120021
'''
'''
output = True
if x < 0:
    ret False
else:
    div, mod = divmod(x, 10*(len(x)))
    d1, m1 = divmod(mod, 10)
    if m1 == div:
        return True
'''
def pointers(x: int) -> bool:
    if x < 0: # or (x % 10 == 0 and x != 0):
        return False
    div = 1
    # only break after overflowing x
    while x >= div * 10: # 1 -> 1000 the most significant
        div *= 10
    while x:
        r = x % 10
        l = x // div
        if r != l:
            return False
        x = (x % div) // 10
        div = div / 100 # chunk out two digits 1000 / 100
        print(x, div)
    return True

def rev_cmp(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    c = x
    b = 0
    while c:
        b = b * 10 + c % 10
        print(b)
        c //= 10
    return b == x

def half_rev_cmp(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    b = 0
    while x > b:
        b = b * 10 + x % 10
        print(b)
        x //= 10
    return b == x or x == b // 10







i = int(input.strip())
print(i)
print(pointers(i))
# print(rev_cmp(i))
# print(half_rev_cmp(i))






# end
