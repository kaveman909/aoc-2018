import re
import sys


class Cart:
    def __init__(self, x, y, direction):
        global g_id
        self.x = x
        self.y = y
        self.position = (x, y)
        self.last_position = (x, y)
        self.direction = direction
        self.next_turn = 'l'
        self.id = g_id
        g_id += 1

    def set_x(self, x):
        self.x = x
        self.last_position = self.position
        self.position = (self.x, self.y)

    def set_y(self, y):
        self.y = y
        self.last_position = self.position
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
g_id = 0
solution = False
# find and initialize all carts
pattern = re.compile(r'[v^<>]')
for y, line in enumerate(track):
    matches = pattern.finditer(line)
    if matches:
        for match in matches:
            x = int(match.span()[0])
            direction = match.group(0)
            carts.append(Cart(x, y, direction))
            # replace cart with appropriate track symbol
            replacement_track = '|' if direction in 'v^' else '-'
            track[y] = track[y].replace(direction, replacement_track)

# main tick
while 1:
    for cart in carts:
        update_position(cart)
    carts_same_spot = list()
    for i, cart in enumerate(carts):
        for j in range(i + 1, len(carts)):
            if (cart.position == carts[j].position) or (cart.position == carts[j].last_position):
                if not solution:
                    print('Part 1: {}'.format(cart.position))
                    solution = True
                for c in [cart, carts[j]]:
                    if c not in carts_same_spot:
                        carts_same_spot.append(c)
    if carts_same_spot != []:
        for cart in carts_same_spot:
            carts.remove(cart)
        if len(carts) == 1:
            print('Part 2: {}'.format(carts[0].position))
            exit()
