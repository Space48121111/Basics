import fileinput
from math import prod
from itertools import count

input = ''' \
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
'''
'''
output = 7 trees X slope: right 3, down 1
output1 = 336 2, 7, 3, 4, and 2 multiplied
..##.........##.........##.........##.........##.........##.......  --->
#..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........X.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...#X....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->

algorithm/ brutal force:
'#': (tx, ty)
while True:
    (x, y) = (x + 3, y - 1)
    if (x, y) = (tx, ty)
    count((tx, ty)) += 1
return count
'''

def trees(r_init, d_init, m):
    r, d, w, t = r_init, d_init, len(m[0]), 0
    while d < len(m):
        t += m[d][r % w] == '#'
        r += r_init
        d += d_init


    return t


def toboggan(right, down, m):
    return sum(
        m[row][col % len(m[row])] == '#'
        for row, col in zip(range(0, len(m), down), count(0, right))
    )


m = [s.strip() for s in input.splitlines()]
# m = [s.strip() for s in fileinput.input('toboggan_coordinate.txt')]
print(trees(3, 1, m))
print(prod(trees(*init, m) for init in ([1, 1], [3, 1], [5, 1], [7, 1], [1, 2])))

print(toboggan(3, 1, m))
print(prod(toboggan(*init, m) for init in ([1, 1], [3, 1], [5, 1], [7, 1], [1, 2])))


# end
