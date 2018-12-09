import string
import difflib

data = [line.strip() for line in open("day-2.txt").readlines()]

twoCount = 0
threeCount = 0

for line in data:
    for letter in string.ascii_lowercase:
        if line.count(letter) == 2:
            twoCount += 1
            break

for line in data:
    for letter in string.ascii_lowercase:
        if line.count(letter) == 3:
            threeCount += 1
            break

print("Part 1: {}".format(twoCount*threeCount))

sm = difflib.SequenceMatcher()
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        sm.set_seq1(data[i])
        sm.set_seq2(data[j])
        matching = sum([k.size for k in sm.get_matching_blocks()])
        if matching == (len(data[i]) - 1):
            similar = ''.join([data[i][k]
                               for k in range(len(data[i])) if data[i][k] == data[j][k]])
            print("Part 2: {}".format(similar))
            exit(0)
