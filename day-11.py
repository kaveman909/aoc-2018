serial_number = 7672
grid_dim = 300
g_power_level_sum = 0
grid = [[0 for _ in range(grid_dim)] for _ in range(grid_dim)]


def get_power_level(x, y):
    rack_id = x + 10
    power_level = (rack_id * y + serial_number) * rack_id
    power_level = (int(str(power_level)[-3]) if power_level >= 100 else 0) - 5
    return power_level


# fill out grid; only need to do once
# (solution is still slow even with pre-computed grid)
for x in range(1, grid_dim + 1):
    for y in range(1, grid_dim + 1):
        grid[y - 1][x - 1] = get_power_level(x, y)

for i in range(3, grid_dim - 1):
    for x_top_left in range(1, grid_dim + 1 - i):
        for y_top_left in range(1, grid_dim + 1 - i):
            power_level_sum = 0
            for x in range(x_top_left, x_top_left + i):
                for y in range(y_top_left, y_top_left + i):
                    power_level_sum += grid[y - 1][x - 1]
            if power_level_sum >= g_power_level_sum:
                g_power_level_sum = power_level_sum
                g_x_top_left = x_top_left
                g_y_top_left = y_top_left
                g_size = i
    if i == 3:
        print('Part 1: {},{}'.format(g_x_top_left, g_y_top_left))
    if g_size != i:
        # this condition may not work for any puzzle input
        print('Part 2: {},{},{}'.format(g_x_top_left, g_y_top_left, g_size))
        break
