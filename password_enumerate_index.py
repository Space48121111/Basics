from __future__ import annotations

txt = open('password.txt', 'r')
input1 = txt.read()

input = ''' \
1-3 a: abcde
1-3 b: cdefg
2-9 c: cbccccccc
'''

'''
output = 2 1st and third ones valid, no instance of b in 2nd
'''

# brutal force
def instruct(s: str) -> int:
    line = s.strip().splitlines()
    valid = 0
    for i, val in enumerate(line):
        range, letter, p = line[i].split()
        min, max = range.split('-')
        l = l[0]
        if l in p:
            c = p.count(l)
            if int(min) <= c <= int(max):
                valid += 1
        '''
        if l not in p:
            print(l, 'Not in a')
        else:
            c = p.count(l)
            if c < int(min) or c > int(max):
                print(l, 'Count out of range')
            else:
                valid += 1
        '''
    return valid

def occurence(s: str) -> int:
    line = s.strip().splitlines()
    valid = 0
    for i, val in enumerate(line):
        r, l, p = line[i].split()
        pos1, pos2 = r.split('-')
        l = l[0]
        if l in p[int(pos1) - 1]:
            valid += 1
        elif l in p[int(pos2) - 1]:
            valid += 1
    return valid


print(occurence(input1))









# end
