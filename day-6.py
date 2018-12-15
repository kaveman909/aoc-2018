data_file = 'day-6.txt'

if data_file == 'day-6-test.txt':
    region = 32
else:
    region = 10000

data = [[int(j) for j in i.strip().split(',')]
        for i in open(data_file).readlines()]

print(data, len(data))

# determine boundaries
x_min, y_min = [min([i[j] for i in data]) for j in range(2)]
x_max, y_max = [max([i[j] for i in data]) + 1 for j in range(2)]

# initialize the grid with 0's
grid = [[0] * x_max for row in range(y_max)]
print('x_min: {}, y_min: {}, x_max: {}, y_max: {}'.format(
    x_min, y_min, x_max, y_max))

# populate grid with closest coordinates per point
# and add boundaries to infinite list
infinite = list()
point_count = [0] * len(data)
region_total = 0
for x in range(x_min, x_max):
    for y in range(y_min, y_max):
        man_dist = list()
        man_accum = 0
        for xp, yp in data:
            man_curr = abs(x - xp) + abs(y - yp)
            man_dist.append(man_curr)
            man_accum += man_curr
        grid[y][x] = man_dist.index(min(man_dist)) if man_dist.count(
            min(man_dist)) == 1 else -1
        if man_accum < region:
            region_total += 1
        if grid[y][x] != -1:
            point_count[grid[y][x]] += 1
            if x in [x_min, x_max - 1] or y in [y_min, y_max - 1]:
                if grid[y][x] not in infinite:
                    infinite.append(grid[y][x])

# for i in grid:
#     print(i)

print('Point Count: {}'.format(point_count))
print('Infinite list: {}'.format(infinite))
max_area = max([point_count[i] if i not in infinite else -
                1 for i in range(len(data))])
print('Part 1: {}'.format(max_area))
print('Part 2: {}'.format(region_total))
