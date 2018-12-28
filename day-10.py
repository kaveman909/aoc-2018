import re

global_size_grid = 1_000_000_000
global_grid = list()


def print_grid():
    for i in global_grid:
        print(''.join(i))


def calc_grid():
    global global_size_grid
    global global_grid
    pos = [[x, y] for [x, y], _ in data]
    # zip(*pos) unzips the pos list; inverse of zip(pos)
    [[x_max, x_min], [y_max, y_min]] = [[f(list(zip(*pos))[i])
                                         for f in [max, min]] for i in range(2)]
    x_grid = x_max - x_min + 1
    y_grid = y_max - y_min + 1
    size_grid = x_grid * y_grid
    if size_grid < global_size_grid and size_grid < 1_000:
        global_size_grid = size_grid
        grid = [[' ' for _ in range(x_grid)] for _ in range(y_grid)]
        for x, y in pos:
            grid[y - y_min][x - x_min] = u"\u2588"
        global_grid = grid[:]
        return True
    return False


data_file = 'day-10.txt'

re_compile = re.compile(
    r'.*[\s<]([\d-]+),\s+([\d-]+).*[\s<]([\d-]+),\s+([\d-]+)')
data = [[[int(re_compile.match(i).group(j + k)) for k in [0, 1]] for j in [1, 3]]
        for i in open(data_file).readlines()]

for time in range(20_000):
    for j, [pos, vel] in enumerate(data):
        pos = [sum(pair) for pair in zip(pos, vel)]
        data[j] = [pos, vel]
    if calc_grid():
        print('Part 1: ')
        print_grid()
        print('Part 2: {}'.format(time + 1))
        break
