from __future__ import annotations
import re

input = ''' \
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
'''

'''
output = 2 valid pass cid optional
algorithm/brutal force:
if key in [hcl, ...]:
    valid += 1
else: not valid
'''

def passport(s: str) -> int:
    fields = {
        'byr': lambda x: 1920 <= int(x) <= 2002,
        'iyr': lambda x: 2010 <= int(x) <= 2020,
        'eyr': lambda x: 2020 <= int(x) <= 2030,
        'hgt': lambda x: (x.endswith('cm') and 150 <= int(x[:-2]) <= 193) or
         (x.endswith('in') and 59 <= int(x[:-2]) <= 76),
        'hcl': lambda x: re.fullmatch(r'#[\da-f]{6}', x),
        'ecl': lambda x: x in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
        'pid': lambda x: re.fullmatch(r'[\d]{9}', x)
    }

    present, valid = 0, 0
    for line in s.strip().split('\n\n'):
        passp = dict(l.split(':') for l in line.split())
        if not passp.keys() >= fields.keys():
            continue
        present += 1
        valid += all(data(passp[field]) for field, data in fields.items())
    return present, valid

txt = open('pass_valid.txt', 'r')
input1 = txt.read()
print(passport(input))





# end
