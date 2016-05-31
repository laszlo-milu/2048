import random
import math
import curses
from curses import KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN
screen = curses.initscr()
curses.start_color()
curses.init_pair(1, 229, curses.COLOR_BLACK)  # color code for number 2
curses.init_pair(2, 227, curses.COLOR_BLACK)  # color code for number 4
curses.init_pair(3, 221, curses.COLOR_BLACK)  # color code for number 8
curses.init_pair(4, 209, curses.COLOR_BLACK)  # color code for number 16
curses.init_pair(5, 203, curses.COLOR_BLACK)  # color code for number 32
curses.init_pair(6, 9, curses.COLOR_BLACK)  # color code for number 64
curses.init_pair(7, 197, curses.COLOR_BLACK)  # color code for number 128
curses.init_pair(8, 161, curses.COLOR_BLACK)  # color code for number 256
curses.init_pair(9, 125, curses.COLOR_BLACK)  # color code for number 512
curses.init_pair(10, 126, curses.COLOR_BLACK)  # color code for number 1024
curses.init_pair(11, 90, curses.COLOR_BLACK)  # color code for number 2048
curses.init_pair(12, curses.COLOR_WHITE, curses.COLOR_BLACK)  # color code for number 0

curses.noecho()
curses.curs_set(0)
win = curses.newwin(12, 22, 0, 0)
# win = curses.newwin(curses.LINES, curses.COLS, 0, 0)
win.keypad(1)
win.border(0)
win.nodelay(1)

numbers = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
'''following line makes testing easier for the colors:
comment out the numbers list filled with zeros and use the following numbers variable instead.'''
# numbers = [[0, 2, 4, 8], [16, 32, 64, 128], [256, 512, 1024, 2048], [0, 0, 0, 0]]

status = 1  # status variable tracks if moving or addition actions were successfully made after a new number was added
color = 0


def move_left(x):  # modified bubble sorting algorithm that moves all the zeros to the right place
    global numbers
    global status
    global valid_move
    exchanges = True
    passnum = len(numbers) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if numbers[x][i] < numbers[x][i + 1] and numbers[x][i] == 0:
                exchanges = True
                temp = numbers[x][i]
                numbers[x][i] = numbers[x][i + 1]
                numbers[x][i + 1] = temp
                status = 1
                valid_move = 0
            else:
                if valid_move == 0:
                    valid_move = valid_move + 1
        passnum = passnum - 1


def move_up(y):  # modified bubble sorting algorithm that moves all the zeros to the right place
    global numbers
    global status
    global valid_move
    exchanges = True
    passnum = len(numbers) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if numbers[i][y] < numbers[i + 1][y] and numbers[i][y] == 0:
                exchanges = True
                temp = numbers[i][y]
                numbers[i][y] = numbers[i + 1][y]
                numbers[i + 1][y] = temp
                status = 1
                valid_move = 0
            else:
                if valid_move == 1:
                    valid_move = valid_move + 1
        passnum = passnum - 1


def move_right(x):  # modified bubble sorting algorithm that moves all the zeros to the right place
    global numbers
    global status
    global valid_move
    exchanges = True
    passnum = len(numbers) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if numbers[x][i] > numbers[x][i + 1] and numbers[x][i + 1] == 0:
                exchanges = True
                temp = numbers[x][i]
                numbers[x][i] = numbers[x][i + 1]
                numbers[x][i + 1] = temp
                status = 1
                valid_move = 0
            else:
                if valid_move == 2:
                    valid_move = valid_move + 1
        passnum = passnum - 1


def move_down(y):  # modified bubble sorting algorithm that moves all the zeros to the right place
    global numbers
    global status
    global valid_move
    exchanges = True
    passnum = len(numbers) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if numbers[i][y] > numbers[i + 1][y] and numbers[i + 1][y] == 0:
                exchanges = True
                temp = numbers[i][y]
                numbers[i][y] = numbers[i + 1][y]
                numbers[i + 1][y] = temp
                status = 1
                valid_move = 0
            else:
                if valid_move == 3:
                    valid_move = valid_move + 1
        passnum = passnum - 1

'''if two numbers are of the same value next to each other in the plane of the pressed key,
this function multiplies one of them by 2 and makes the other number a zero.'''


def add_left(x):
    global numbers
    global status
    global valid_move
    for i in range(3):
        if numbers[x][i] == numbers[x][i + 1] and numbers[x][i] != 0:
            numbers[x][i] = numbers[x][i] * 2
            numbers[x][i + 1] = 0
            status = 1
            valid_move = 0
        else:
            if valid_move == 0:
                valid_move = valid_move + 1

'''if two numbers are of the same value next to each other in the plane of the pressed key,
this function multiplies one of them by 2 and makes the other number a zero.'''


def add_up(y):
    global numbers
    global status
    global valid_move
    for i in range(3):
        if numbers[i][y] == numbers[i + 1][y] and numbers[i][y] != 0:
            numbers[i][y] = numbers[i][y] * 2
            numbers[i + 1][y] = 0
            status = 1
            valid_move = 0
        else:
            if valid_move == 1:
                valid_move = valid_move + 1

'''if two numbers are of the same value next to each other in the plane of the pressed key,
this function multiplies one of them by 2 and makes the other number a zero.'''


def add_right(x):
    global numbers
    global status
    global valid_move
    for i in reversed(range(3)):
        if numbers[x][i] == numbers[x][i + 1] and numbers[x][i + 1] != 0:
            numbers[x][i + 1] = numbers[x][i + 1] * 2
            numbers[x][i] = 0
            status = 1
            valid_move = 0
        else:
            if valid_move == 2:
                valid_move = valid_move + 1

'''if two numbers are of the same value next to each other in the plane of the pressed key,
this function multiplies one of them by 2 and makes the other number a zero.'''


def add_down(y):
    global numbers
    global status
    global valid_move
    for i in reversed(range(3)):
        if numbers[i][y] == numbers[i + 1][y] and numbers[i][y] != 0:
            numbers[i + 1][y] = numbers[i + 1][y] * 2
            numbers[i][y] = 0
            status = 1
            valid_move = 0
        else:
            if valid_move == 3:
                valid_move = valid_move + 1


def key_left_pressed():  # what happens when the given key is pressed
    global status
    for x in range(4):
        move_left(x)
        add_left(x)
        move_left(x)
    add_new_number()


def key_right_pressed():  # what happens when the given key is pressed
    global status
    for x in range(4):
        move_right(x)
        add_right(x)
        move_right(x)
    add_new_number()


def key_up_pressed():  # what happens when the given key is pressed
    global status
    for y in range(4):
        move_up(y)
        add_up(y)
        move_up(y)
    add_new_number()


def key_down_pressed():  # what happens when the given key is pressed
    global status
    for y in range(4):
        move_down(y)
        add_down(y)
        move_down(y)
    add_new_number()


def add_new_number():
    global numbers
    global status
    global highest
    global valid_move

    two_or_four = random.randrange(10)
    y = random.randrange(4)  # These two generate a random coordinate for the new numeber to be added.
    x = random.randrange(4)

    if numbers[y][x] == 0 and status == 1:
        if two_or_four != 1:
            numbers[y][x] = 2
        else:
            numbers[y][x] = 4  # with a 10% chance of adding a 4
        status = 0
        valid_move = 0
        highest = max(numbers)
        win.addstr(10, 1, "                   ")

    elif status == 1:
        add_new_number()
        win.addstr(10, 1, "                   ")
    else:
        status = 2
        if status == 2:
            win.addstr(10, 1, "Try other direction")


def colors(num):
    if num == 0:
        return 12
    else:
        return int(math.log2(num))

add_new_number()
status = 1
add_new_number()
win.addstr(10, 1, "                   ")
win.addstr(10, 1, "Press ESC to quit")
while True:

    ch = win.getch()
    for y in range(4):
        for x in range(4):
            color = colors(numbers[y][x])
            win.addstr(1 + y * 2, 1 + x * 5, "     ")
            win.addstr(1 + y * 2, 1 + x * 5, str(numbers[y][x]), curses.color_pair(color))

    if ch == curses.KEY_LEFT:
        key_left_pressed()

    if ch == curses.KEY_RIGHT:
        key_right_pressed()

    if ch == curses.KEY_UP:
        key_up_pressed()

    if ch == curses.KEY_DOWN:
        key_down_pressed()

    if valid_move == 4:
        win.addstr(10, 1, "                   ")
        win.addstr(10, 1, "Game over!", curses.A_BOLD)

    if ch == 27:
        break

curses.endwin()
