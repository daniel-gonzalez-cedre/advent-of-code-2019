def part1(init, x = 12, y = 2):
    data = init.copy()
    i = 0
    data[1] = x
    data[2] = y
    while i < len(data):
        if data[i] == 1:
            data[data[i + 3]] = data[data[i + 1]] + data[data[i + 2]]
            i = i + 4
        elif data[i] == 2:
            data[data[i + 3]] = data[data[i + 1]] * data[data[i + 2]]
            i = i + 4
        else:
            return data[0]

def part2(data):
    for x in range(100):
        for y in range(100):
            z = part1(data, x, y)
            if z == 19690720:
                return (x, y)
    return (-1, -1)

def main():
    with open('input.txt') as f:
        data = [int(x) for lines in f for x in lines.strip().split(',')]
        sol = part1(data)
        noun, verb = part2(data)
        print('result 1: ', sol)
        print('result 2: ', 100*noun + verb)

main()
