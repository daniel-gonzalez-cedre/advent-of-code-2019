import numpy as np

def fuel(d):
    f = 0
    while d//3 - 2 > 0:
        d = d//3 - 2
        f = f + d
    return f

def part1(data):
    return np.sum(data//3 - 2)

def part2(data):
    return sum(map(fuel, data))

def main():
    with open('./input.txt') as f:
        data = np.asarray([int(lines.strip()) for lines in f])
        print('part 1:\t{}'.format(part1(data)))
        print('part 2:\t{}'.format(part2(data)))

main()
