from operator import add, itemgetter


def run_part(part, func):
    book_func = {entry: func(book[entry]) for entry in book}
    max_entry = max(book_func.items(), key=itemgetter(1))[0]
    max_minute = book[max_entry].index(max(book[max_entry]))

    print("Part {}: {}".format(part, int(max_entry) * max_minute))


data = [line.strip().split('\t') for line in open("day-4.txt").readlines()]
data = [[int(i[0]), i[1]] for i in data]
asleep = 'falls asleep'
wakes = 'wakes up'
current_key = 'error'
book = dict()
MINUTES = 60

for time, event in data:
    if asleep in event:
        a_time = time
    elif wakes in event:
        w_time = time
        asleep_list = [1 if (i >= a_time) and (i < w_time)
                       else 0 for i in range(MINUTES)]
        book[current_key] = list(map(add, book[current_key], asleep_list))
    else:
        current_key = event
        if current_key not in book:
            book[current_key] = [0] * MINUTES

run_part(1, sum)
run_part(2, max)
