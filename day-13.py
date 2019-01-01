import re
import sys


class Cart:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.position = (x, y)
        self.direction = direction
        self.next_turn = 'l'

    def set_x(self, x):
        self.x = x
        self.position = (self.x, self.y)

    def set_y(self, y):
        self.y = y
        self.position = (self.x, self.y)


def rotate_cart(cart):
    if cart.next_turn == 'l':
        if cart.direction == '^':
            cart.direction = '<'
        elif cart.direction == '<':
            cart.direction = 'v'
        elif cart.direction == 'v':
            cart.direction = '>'
        elif cart.direction == '>':
            cart.direction = '^'
        cart.next_turn = 's'
    elif cart.next_turn == 's':
        # direction stays the same
        cart.next_turn = 'r'
    elif cart.next_turn == 'r':
        if cart.direction == '^':
            cart.direction = '>'
        elif cart.direction == '>':
            cart.direction = 'v'
        elif cart.direction == 'v':
            cart.direction = '<'
        elif cart.direction == '<':
            cart.direction = '^'
        cart.next_turn = 'l'


def check_for_rotate(cart):
    current_track = track[cart.y][cart.x]
    if current_track == '/':
        if cart.direction == '^':
            cart.direction = '>'
        elif cart.direction == '>':
            cart.direction = '^'
        elif cart.direction == '<':
            cart.direction = 'v'
        elif cart.direction == 'v':
            cart.direction = '<'
    elif current_track == '\\':
        if cart.direction == '>':
            cart.direction = 'v'
        elif cart.direction == 'v':
            cart.direction = '>'
        elif cart.direction == '^':
            cart.direction = '<'
        elif cart.direction == '<':
            cart.direction = '^'
    elif current_track == '+':
        rotate_cart(cart)


def update_position(cart):
    if cart.direction == 'v':
        cart.set_y(cart.y + 1)
    elif cart.direction == '^':
        cart.set_y(cart.y - 1)
    elif cart.direction == '<':
        cart.set_x(cart.x - 1)
    elif cart.direction == '>':
        cart.set_x(cart.x + 1)

    check_for_rotate(cart)


track = [i.strip('\n') for i in open('day-13.txt').readlines()]
carts = list()
solution = False
# find and initialize all carts
pattern = re.compile(r'[v^<>]')
for y, line in enumerate(track):
    matches = pattern.search(line)
    if matches:
        x = int(matches.span()[0])
        direction = matches.group(0)
        carts.append(Cart(x, y, direction))
        # replace cart with appropriate track symbol
        replacement_track = '|' if direction in 'v^' else '-'
        track[y] = track[y].replace(direction, replacement_track)
for i, line in enumerate(track):
    print(i, line)

# main tick
for k in range(10000):
    # print('Iteration:', k)
    for i, cart in enumerate(carts):
        # if i == 14:
        #     print(i, cart.position, cart.direction,
        #           cart.next_turn, track[cart.y][cart.x])
        update_position(cart)
    carts_copy = carts[:]
    for i, cart in enumerate(carts_copy):
        for j in range(i + 1, len(carts_copy)):
            if cart.position == carts_copy[j].position:
                if not solution:
                    print('Part 1: {}'.format(cart.position))
                    solution = True
                cart2 = carts_copy[j]
                carts.remove(cart)
                carts.remove(cart2)
                if len(carts) == 1:
                    print('Part 2: {}'.format(carts[0].position))
                    print(carts[0].direction, carts[0].next_turn,
                          carts[0].x, carts[0].y, carts[0].position)
                    exit()
