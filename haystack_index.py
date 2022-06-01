# haystack = "hello"
# haystack = "aaaaa"
haystack = "mississipi"

# haystack = ''
# needle = 'll'
needle = 'issip'

def indices_range(hay, nee):
    if hay == None or nee not in hay:
        return -1
    else:
        for i in range(len(hay) - len(nee) + 1):
            if nee == hay[i: i + len(nee)]:
                return i

print(indices_range(haystack,  needle))

def index(hay, nee):
    if hay == None or nee not in hay:
        return -1
    else:
        for i in range(len(hay)):
            for j in range(len(nee)):
                print(i, j, hay[i], nee[j])
                if nee[j] == hay[i]:
                    return i

# print(index(haystack,  needle))




# end
