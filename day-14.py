from collections import deque

total_recipes = 556061
initial_scores = [3, 7]
recipes = initial_scores[:]
print(recipes)
elf_recipes = initial_scores[:]
elf_positions = [0, 1]
print(elf_recipes)
while(len(recipes) < total_recipes + 10):
    sum_scores = str(sum(elf_recipes))
    new_scores = [int(sum_scores[i]) for i in range(len(sum_scores))]
    for i in new_scores:
        recipes.append(i)
    # print(sum_scores, new_scores, recipes)
    for i in range(len(elf_recipes)):
        elf_positions[i] = (elf_positions[i] + elf_recipes[i] + 1) % len(recipes)
        elf_recipes[i] = recipes[elf_positions[i]]
    # print(elf_positions, elf_recipes)
print(''.join([str(i) for i in recipes[total_recipes:total_recipes + 10]]))
