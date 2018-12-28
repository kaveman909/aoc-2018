import re
from collections import deque
data_file = 'day-9.txt'

match = re.match(r'(\d+)\b.*\b(\d+)', open(data_file).readline())
players, last_marble = [int(match.group(i)) for i in range(1, 3)]
# players, last_marble = [9, 25]
score_list = [0] * players
marble_deque = deque([0])
current_player = 0

for marble in range(1, last_marble + 1):
    if (marble % 23) == 0:
        score_list[current_player] += marble
        marble_deque.rotate(7)
        score_list[current_player] += marble_deque[0]
        marble_deque.popleft()
    else:
        marble_deque.rotate(-2)
        marble_deque.append(marble)
        marble_deque.rotate(1)
        # print(current_player + 1, marble_deque)
    current_player = (current_player + 1) % players
    # if marble == last_marble:
    #     print("Part 1: {}".format(max(score_list)))
print("Part 1: {}".format(max(score_list)))
