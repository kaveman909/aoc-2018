import re


def get_next_gen(pots, pos):
    mask = 0b11111
    shifted_pots = pots >> (pos - (mask_size - 1))
    return rules[shifted_pots & mask]


pot_buffer = 3
mask_size = 5
pots_added_to_right = 0
pattern = re.compile(r'([#.]+)')
data = [i.strip() for i in open('day-12.txt').readlines()]
# int(x, 2) converts base-2 string (ex. '101') to base-2 int (ex. 5)
pots = int(pattern.search(data[0]).group(
    1).replace('#', '1').replace('.', '0'), 2)
pot_count = len('{0:b}'.format(pots))
rules = list()
for i in range(2, len(data)):
    rules.append([int(j.replace('#', '1').replace('.', '0'), 2)
                  for j in pattern.findall(data[i])])
rules.sort()
rules = [i[1] for i in rules]
# during debugging, it was noticed that the pot configuration was the same every 10000
# iterations.  So, we can "skip ahead" and adjust for the 50 billion case
for i in range(10000):
    pots_temp = pots << pot_buffer
    pot_count_temp = len('{0:b}'.format(pots_temp)) + pot_buffer
    pots_next_gen = 0

    for pos in range(mask_size - 1, pot_count_temp):
        pots_next_gen = pots_next_gen | (
            get_next_gen(pots_temp, pos) << (pos - (mask_size - 1)))
    shift_count = 0
    while (pots_next_gen & 1) == 0:
        pots_next_gen = pots_next_gen >> 1
        shift_count += 1
    # could be negative (pots could have been removed from right)
    pots_added_to_right += (1 - shift_count)
    pots = pots_next_gen
    if (i == 19):
        first_pot = pot_count + pots_added_to_right - len('{0:b}'.format(pots))
        print('Part 1: {}'.format(sum([int(j)*(first_pot + i)
                                       for i, j in enumerate('{0:b}'.format(pots))])))
# we make an assumption about how many pots were added to the right, based
# on the observation that on every generation except the 1st, a pot has
# been added on the right
pots_added_to_right = 50000000000 - 1
first_pot = pot_count + pots_added_to_right - len('{0:b}'.format(pots))
print('Part 2: {}'.format(sum([int(j)*(first_pot+i)
                               for i, j in enumerate('{0:b}'.format(pots))])))
