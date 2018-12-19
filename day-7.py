import re
import string


class Elf:

    def __init__(self):
        self.time = 0
        self.letter = idle_letter


N = 5
T = 60
# letter_list = 'ABCDEF'
letter_list = string.ascii_uppercase
idle_letter = '.'
data = [i.strip() for i in open('day-7.txt').readlines()]
regex_string = r'\b([A-Z])\b.*\b([A-Z])\b'
regex_object = re.compile(regex_string)
recipe = list()
for i in data:
    match_object = regex_object.search(i)
    recipe.append([match_object.group(j) for j in range(1, 3)])
recipe.sort(key=lambda x: (x[1], x[0]))

recipe_dict = {i: list() for i in letter_list}
for prereq, step in recipe:
    recipe_dict[step].append(prereq)

letters_used = list()
letters_left = list(letter_list)
while letters_left != []:
    for letter in letters_left:
        can_use = True
        for i in recipe_dict[letter]:
            if i not in letters_used:
                can_use = False
                break
        if can_use:
            letters_used.append(letter)
            letters_left.remove(letter)
            break
letters_used = ''.join(letters_used)
print('Part 1: {}'.format(letters_used))

t = 0
elves = [Elf() for i in range(N)]
letters_used = list()
letters_done = list(letter_list)
letters_left = list(letter_list)
while letters_done != []:
    # check if any worker is done
    for worker in elves:
        if worker.time > 0:
            worker.time -= 1
        if worker.time == 0 and worker.letter != idle_letter:
            letters_used.append(worker.letter)
            letters_done.remove(worker.letter)
            worker.letter = idle_letter
    # check if there are any letter to grab, by a free worker
    letters_left_copy = letters_left[:]
    for letter in letters_left_copy:
        can_use = True
        for i in recipe_dict[letter]:
            if i not in letters_used:
                can_use = False
                break
        if can_use:
            # check for free worker
            for worker in elves:
                if worker.time == 0:
                    letters_left.remove(letter)
                    worker.time = T + letter_list.index(letter) + 1
                    worker.letter = letter
                    break
    t += 1
    print(t - 1, end='\t')
    for worker in elves:
        print(worker.letter, end='\t')
    print(''.join(letters_used))

print("Part 2: {}".format(t - 1))
for recipe in recipe_dict:
    print(recipe, recipe_dict[recipe])
