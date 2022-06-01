# haystack = "hello"
# haystack = "aaaaa"
haystack = "mississipi"

# haystack = ''
# needle = 'll'
needle = 'issip'

def indices_range(hay, nee):
    if nee == '':
        return 0

    for i in range(len(hay) - len(nee) + 1):
        if nee == hay[i: i + len(nee)]:
            return i
     return -1

print(indices_range(haystack,  needle))

def index(hay, nee):
    if hay == None or nee not in hay:
        return 0

    for i in range(len(hay)):
        for j in range(len(nee)):
            if hay[i + j] != nee[j]:
                print('Not equal')
                break
            if j == len(nee) - 1:
                print('Equal')
                return i
    return -1

print(index(haystack,  needle))




# end
