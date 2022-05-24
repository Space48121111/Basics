from __future__ import annotations
from collections import Counter
from itertools import product

input = ''' \
.#.
..#
###
'''
'''
output = 112 active state cubes after z 0-6 cycles
27-1 neighbors: inactive
if ac n 2 or 3 neighb ac: a
if ina n 3 neighb ac: a
algorithms/brutal force:
coords: yield x-1, x, x+1 y z pts = (x, y, z)
'#' = ina ',' = ac
for pts in inp:
    while i <= 6:
        state = ina
        count[n.s_ac] = 0
            for neighb in coords:
                if state = ac and count[neighb] == 2 or 3:
                    state = ac
                elif state = ina and count[neighb] == 3:
                    state = ac
        i += 1
count[ac]
return count

'''

def compute(line: str, dim: int) ->int:
    zeros = [0] * (dim - 2)
    # combinatoric iterators cartesian coords prod -> lexicographic ordered
    # prod(arr, repeat) -> (arr1, arr2, arr3)
    coords = {*product((-1, 0, 1), repeat = dim)} - {(0, 0, *zeros)}
    cubes = {(row, col, *zeros) for col, line in enumerate(lines) \
    for row, char in enumerate(line) if char == '#'}
    for _ in range(6):
        # tuple: immutable can't changed set: no dup can't repeat
        neighbors = Counter(tuple(sum(x) for x in zip(cube, coord)) \
         for cube in cubes for coord in coords)
        cubes = {ne for ne, ct in neighbors.items() if ct == 3 or \
        (ct == 2 and ne in cubes)}
    return len(cubes) # + len(coords)

lines = input.splitlines()
input1 = open('3d_cube.txt', 'r').read()
# lines = input1.splitlines()

print(compute(lines, 3))
print(compute(lines, 4))










# end
