import random
import math
import curses
from time import sleep
from curses import KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN
screen = curses.initscr()
curses.start_color()
curses.use_default_colors()
curses.init_pair(1, 229, -1)  # color code for number 2
curses.init_pair(2, 227, -1)  # color code for number 4
curses.init_pair(3, 221, -1)  # color code for number 8
curses.init_pair(4, 209, -1)  # color code for number 16
curses.init_pair(5, 203, -1)  # color code for number 32
curses.init_pair(6, 9, -1)  # color code for number 64
curses.init_pair(7, 197, -1)  # color code for number 128
curses.init_pair(8, 161, -1)  # color code for number 256
curses.init_pair(9, 125, -1)  # color code for number 512
curses.init_pair(10, 126, -1)  # color code for number 1024
curses.init_pair(11, 90, -1)  # color code for number 2048
curses.init_pair(12, curses.COLOR_WHITE, -1)  # color code for number 0
curses.noecho()
curses.curs_set(0)
win = curses.newwin(13, 22, 0, 0)
win.keypad(1)
win.border(0)
win.nodelay(1)


def move_left(x):  # modified bubble sorting algorithm that moves all the zeros to the right place
    global numbers
    global action
    global invalid_move_left
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
                action = 1
                invalid_move_left = False
        passnum = passnum - 1


def move_up(y):  # modified bubble sorting algorithm that moves all the zeros to the right place
    global numbers
    global action
    global invalid_move_up
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
                action = 1
                invalid_move_up = False
        passnum = passnum - 1


def move_right(x):  # modified bubble sorting algorithm that moves all the zeros to the right place
    global numbers
    global action
    global invalid_move_right
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
                action = 1
                invalid_move_right = False
        passnum = passnum - 1


def move_down(y):  # modified bubble sorting algorithm that moves all the zeros to the right place
    global numbers
    global action
    global invalid_move_down
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
                action = 1
                invalid_move_down = False
        passnum = passnum - 1


def add_left(x):
    '''if two numbers are of the same value next to each other in the plane of the pressed key,
    this function multiplies one of them by 2 and makes the other number a zero.'''
    global numbers
    global action
    global invalid_move_left
    score_to_add = 0
    for i in range(3):
        if numbers[x][i] == numbers[x][i + 1] and numbers[x][i] != 0:
            numbers[x][i] = numbers[x][i] * 2
            numbers[x][i + 1] = 0
            score_to_add = score_to_add + numbers[x][i]
            score_added(score_to_add)
            action = 1
            invalid_move_left = False


def add_up(y):
    '''if two numbers are of the same value next to each other in the plane of the pressed key,
    this function multiplies one of them by 2 and makes the other number a zero.'''
    global numbers
    global action
    global invalid_move_up
    score_to_add = 0
    for i in range(3):
        if numbers[i][y] == numbers[i + 1][y] and numbers[i][y] != 0:
            numbers[i][y] = numbers[i][y] * 2
            numbers[i + 1][y] = 0
            score_to_add = score_to_add + numbers[i][y]
            score_added(score_to_add)
            action = 1
            invalid_move_up = False


def add_right(x):
    '''if two numbers are of the same value next to each other in the plane of the pressed key,
    this function multiplies one of them by 2 and makes the other number a zero.'''
    global numbers
    global action
    global invalid_move_right
    score_to_add = 0
    for i in reversed(range(3)):
        if numbers[x][i] == numbers[x][i + 1] and numbers[x][i + 1] != 0:
            numbers[x][i + 1] = numbers[x][i + 1] * 2
            numbers[x][i] = 0
            score_to_add = score_to_add + numbers[x][i + 1]
            score_added(score_to_add)
            action = 1
            invalid_move_right = False


def add_down(y):
    '''if two numbers are of the same value next to each other in the plane of the pressed key,
    this function multiplies one of them by 2 and makes the other number a zero.'''
    global numbers
    global action
    global invalid_move_down
    score_to_add = 0
    for i in reversed(range(3)):
        if numbers[i][y] == numbers[i + 1][y] and numbers[i][y] != 0:
            numbers[i + 1][y] = numbers[i + 1][y] * 2
            numbers[i][y] = 0
            score_to_add = score_to_add + numbers[i + 1][y]
            score_added(score_to_add)
            action = 1
            invalid_move_down = False


def score_added(score_to_add):
    global score
    score = score + score_to_add
    text = "Score: " + str(score)
    win.addstr(10, 1, int((20-len(text))/2)*" " + text)


def key_left_pressed():  # what happens when the given key is pressed
    global action
    global invalid_move_left
    global invalid_move
    invalid_move_left = True
    for x in range(4):
        move_left(x)
        add_left(x)
        move_left(x)
    add_new_number()
    if not invalid_move_left or not invalid_move_right or not invalid_move_down or not invalid_move_up:
        invalid_move = False
    else:
        invalid_move = True
    action = 0


def key_right_pressed():  # what happens when the given key is pressed
    global action
    global invalid_move_right
    global invalid_move
    invalid_move_right = True
    for x in range(4):
        move_right(x)
        add_right(x)
        move_right(x)
    add_new_number()
    if not invalid_move_left or not invalid_move_right or not invalid_move_down or not invalid_move_up:
        invalid_move = False
    else:
        invalid_move = True
    action = 0


def key_up_pressed():  # what happens when the given key is pressed
    global action
    global invalid_move_up
    global invalid_move
    invalid_move_up = True
    for y in range(4):
        move_up(y)
        add_up(y)
        move_up(y)
    add_new_number()
    if not invalid_move_left or not invalid_move_right or not invalid_move_down or not invalid_move_up:
        invalid_move = False
    else:
        invalid_move = True
    action = 0


def key_down_pressed():  # what happens when the given key is pressed
    global action
    global invalid_move_down
    global invalid_move
    invalid_move_down = True
    for y in range(4):
        move_down(y)
        add_down(y)
        move_down(y)
    add_new_number()
    if not invalid_move_left or not invalid_move_right or not invalid_move_down or not invalid_move_up:
        invalid_move = False
    else:
        invalid_move = True
    action = 0


def add_new_number():
    global numbers
    global action
    global highest
    global invalid_move
    global color
    global autoplayer
    global double
    two_or_four = random.randrange(10)
    y = random.randrange(4)  # These two generate a random coordinate for the new numeber to be added.
    x = random.randrange(4)
    if not double:
        printing()
    if numbers[y][x] == 0 and action == 1:
        if two_or_four != 1:
            numbers[y][x] = 2
            color = colors(numbers[y][x])
        else:
            numbers[y][x] = 4  # with a 10% chance of adding a 4
            color = colors(numbers[y][x])
        attributes = curses.color_pair(color) | curses.A_BOLD | curses.A_UNDERLINE
        win.addstr(1 + y * 2, 1 + x * 5, str(numbers[y][x]), attributes)
        action = 0
        reset_invalid()
        highest = max(numbers)
        win.addstr(9, 1, "                    ")

    elif action == 1:
        add_new_number()
        win.addstr(9, 1, "                    ")
    else:
        action = 2
        if action == 2 and invalid_move_left or invalid_move_right or invalid_move_down or invalid_move_up:
            if not autoplayer:
                win.addstr(9, 1, "Try other direction ")
            if flashing:
                curses.flash()


def colors(num):
    if num == 0:
        return 12
    else:
        return int(math.log2(num))


def reset_invalid():
    global invalid_move_down
    global invalid_move_right
    global invalid_move_up
    global invalid_move_left
    invalid_move_right = False
    invalid_move_down = False
    invalid_move_left = False
    invalid_move_up = False


def restart(re=False):
    global numbers
    global action
    global flashing
    global autoplayer
    global delay
    global score
    global double
    global invalid_move
    reset_invalid()
    invalid_move = False
    numbers = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    '''following line makes testing easier for the colors and game over:
    comment out the numbers list filled with zeros and use the following numbers variable instead.'''
    # numbers = [[0, 2, 4, 8], [16, 32, 64, 128], [256, 512, 1024, 1024], [0, 0, 0, 1024]]
    score = 0
    action = 1  # action variable tracks if valid action was made after a new number was added
    printing()
    double = True
    add_new_number()
    action = 1
    add_new_number()
    if not re:
        color = 0
        flashing = True
        win.addstr(8, 1, "                    ", curses.A_UNDERLINE)
        win.addstr(9, 1, "   Do you want to   ")
        win.addstr(10, 1, "  enable autoplay?  ")
        win.addstr(11, 1, "       (y/n)        ")
        ch = win.getch()
        while ch != 121 or 110:
            ch = win.getch()
            if ch == 121:
                flashing = False
                autoplayer = True
                win.addstr(9, 1, " Instant  autoplay? ")
                win.addstr(10, 1, "       (y/n)        ")
                win.addstr(11, 1, "                    ")
                ch = win.getch()
                while ch != 121 or 110:
                    ch = win.getch()
                    if ch == 121:
                        delay = 0
                        break
                    if ch == 110:
                        delay = 0.5
                        break
                break

            if ch == 110:
                autoplayer = False
                break
        if flashing:
            win.addstr(9, 1, "Are you sensitive to")
            win.addstr(10, 1, "  flashing lights?  ")
            win.addstr(11, 1, "       (y/n)        ")
            ch = win.getch()
            while ch != 121 or 110:
                ch = win.getch()
                if ch == 121:
                    flashing = False
                    break
                if ch == 110:
                    flashing = True
                    break

    double = False
    win.addstr(9, 1, "                    ")
    win.addstr(10, 1, "                    ")
    win.addstr(11, 1, "reset=r     exit=esc", curses.A_DIM)
    win.addstr(11, 7, "r", curses.A_BOLD)
    win.addstr(11, 18, "esc", curses.A_BOLD)
    score_added(0)
    if re:
        return
    else:
        monitoring()


def printing():
    for y in range(4):
        for x in range(4):
            color = colors(numbers[y][x])
            attributes = curses.color_pair(color)
            win.addstr(1 + y * 2, 1 + x * 5, "     ")
            if numbers[y][x] == 0:
                attributes = curses.color_pair(color) | curses.A_DIM
            elif numbers[y][x] > 2048:
                attributes = curses.color_pair(12)
            win.addstr(1 + y * 2, 1 + x * 5, str(numbers[y][x]), attributes)


def monitoring():
    global numbers
    global invalid_move
    global autoplayer
    global delay
    while True:
        ch = win.getch()
        if autoplayer and not invalid_move:
            win.addstr(11, 9, "   ")
            win.addstr(10, 1, "  ")
            win.addstr(9, 9, "   ")
            win.addstr(10, 19, "  ")
            autoplay()
            sleep(delay)

        for y in range(4):
            for x in range(4):
                if numbers[y][x] == 2048:
                    invalid_move = True
                    victory = True
                    game_over(victory)

        if invalid_move:
            victory = False
            game_over(victory)

        if ch == 27:
            break

        if ch == 114:
            win.addstr(9, 1, "Are you sure? (y/n) ")
            while ch != 121 or 110:
                ch = win.getch()
                if ch == 121:
                    restart(True)
                    break
                if ch == 110:
                    win.addstr(9, 1, "                    ")
                    break
        win.refresh()

        if not autoplayer:
            if not invalid_move:
                if ch == curses.KEY_LEFT:
                        key_left_pressed()
                if ch == curses.KEY_RIGHT:
                        key_right_pressed()
                if ch == curses.KEY_UP:
                        key_up_pressed()
                if ch == curses.KEY_DOWN:
                        key_down_pressed()


def game_over(victory=False):
    global invalid_move_up
    global invalid_move_left
    global invalid_move_down
    global invalid_move_right
    win.addstr(11, 9, "   ")
    win.addstr(10, 1, "   ")
    win.addstr(9, 9, "   ")
    win.addstr(10, 19, "  ")
    if victory and not invalid_move_left or not invalid_move_right or not invalid_move_down or not invalid_move_up:
        win.addstr(9, 1, "  Congratulations!  ", curses.A_BOLD)
    else:
        win.addstr(9, 1, "     Game  Over     ", curses.A_BOLD)
    win.refresh()


def autoplay():
    global invalid_move_up
    global invalid_move_left
    global invalid_move_down
    global invalid_move_right
    # next_move = random.randrange(5)
    # if next_move == 1:
    #     key_left_pressed()
    # if next_move == 2:
    #     key_right_pressed()
    # if next_move == 3:
    #     key_up_pressed()
    # if next_move == 4:
    #     key_down_pressed()
    # sleep(0.2)
    # *************************************
    key_left_pressed()
    win.addstr(10, 1, "<")
    if invalid_move_left:
        key_down_pressed()
        win.addstr(10, 1, "  ")
        win.addstr(11, 11, "v")
        if invalid_move_down:
            key_right_pressed()
            win.addstr(11, 10, "   ")
            win.addstr(10, 20, ">")
            if invalid_move_right:
                key_up_pressed()
                win.addstr(10, 19, "  ")
                win.addstr(9, 11, "∧")

restart()
curses.endwin()
