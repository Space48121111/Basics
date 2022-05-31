def validate(ls):
    if ls[0] == 6 or ls[len(ls) - 1] == 6:
        return True
    else:
        return False
print(validate([1, 2, 6]))
print(validate([6, 1, 2, 3]))
print(validate([13, 6, 1, 2, 3]))

def cmp(ls1, ls2):
    if ls1[0] == ls2[0] or ls1[len(ls1) - 1] == ls2[len(ls2) - 1]:
        return True
    else:
        return False
print(cmp([1, 2, 3], [7, 3]))
print(cmp([1, 2, 3], [7, 3, 2]))
print(cmp([1, 2, 3], [1, 3]))

def reverse(ls):
    new_ls_c = ls.copy()
    new_ls = list(reversed(new_ls_c))
    print(new_ls)
reverse([1, 2, 3])
reverse([5, 11, 9])
reverse([7, 0, 0])

def palindrome(ls):
    if len(ls) >= 1:
        if ls[0] == ls[len(ls) - 1]:
            return True
        else:
            return False
    return False
print(palindrome([1, 2, 3]))
print(palindrome([1, 2, 3, 1]))
print(palindrome([1, 2, 1]))

def sum_int(ls):
    t = 0
    for num in ls:
        t += num
    return t

print(sum_int([1, 2, 3]))
print(sum_int([5, 11, 2]))
print(sum_int([7, 0, 0]))


def grocery_ls():
    # ls = []
    while True:
        inp = input('Please give me 5 grocery items(Separate them by space): ')
        items = inp.split()
        # ls.append(item)
        if len(items) == 5:
            print("Here're your checkout items: ", items)
            # break
        else:
            print('I do not get it, 5 items plz.', inp)

# grocery_ls()

def sum(ls):
    res = 0
    for val in ls:
        res += int(val)
    return res

# print(sum([2, 3, -3]))


def remove_dup():
    ls = [10,20,30,20,10,50,60,40,80,50,40]
    unique = set(ls)
    new_ls = list(unique)
    return new_ls


# print(remove_dup())




# end
