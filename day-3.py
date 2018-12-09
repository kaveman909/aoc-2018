data = [line.strip() for line in open("day-3.txt").readlines()]
N = 1000
pos = []
size = []
area = []
rows = len(data)
matches = [0] * rows

# Parse input for position and sizes of patches in usable list format
for line in data:
    line1 = line.split(' @ ')[1].split(': ')
    pos.append([int(i) for i in line1[0].split(',')])
    size.append([int(i) for i in line1[1].split('x')])
    area.append(size[-1][0] * size[-1][1])

# Start with a "blank" quilt
quilt = [[0] * N for i in range(N)]
quilt_id = [[0] * N for i in range(N)]

for id, ([px, py], [sx, sy]) in enumerate(zip(pos, size), 1):
    for x in range(px, px + sx):
        for y in range(py, py + sy):
            quilt[y][x] += 1
            quilt_id[y][x] += id

dups = [[1 if i > 1 else 0 for i in quilt[j]] for j in range(N)]

print("Part 1: {}".format(sum(map(sum, dups))))

for id, ([px, py], [sx, sy]) in enumerate(zip(pos, size), 1):
    for x in range(px, px + sx):
        for y in range(py, py + sy):
            if quilt_id[y][x] == id:
                matches[id - 1] += 1
    if matches[id - 1] == area[id - 1]:
        print("Part 2: {}".format(id))
