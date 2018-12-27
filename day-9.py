import re
data_file = 'day-9.txt'

match = re.match(r'(\d+)\b.*\b(\d+)', open(data_file).readline())
players, last_marble = [int(match.group(i)) for i in range(1, 3)]
score_list = [0] * players
marble_list = [0]  # start with 0 placed
current_marble = 0
current_player = 0

for marble in range(1, last_marble + 1):
    current_marble_index = marble_list.index(current_marble)
    if (marble % 23) == 0:
        score_list[current_player] += marble
        remove_marble_index = current_marble_index - 7
        if remove_marble_index < 0:
            remove_marble_index += len(marble_list)
        score_list[current_player] += marble_list[remove_marble_index]
        marble_list.pop(remove_marble_index)
        current_marble = marble_list[remove_marble_index]
    else:
        new_marble_index = (current_marble_index + 2) % len(marble_list)
        marble_list.insert(new_marble_index, marble)
        current_marble = marble
    # print(current_player + 1, marble_list)
    current_player = (current_player + 1) % players
print("Part 1: {}".format(max(score_list)))
