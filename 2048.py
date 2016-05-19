import curses
from curses import KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN
screen = curses.initscr()
curses.noecho()
curses.curs_set(0)
win = curses.newwin(curses.LINES, curses.COLS, 0, 0)
win.keypad(1)
win.border(0)
win.nodelay(1)
import random

def key_left_pressed():

def key_right_pressed():

def key_up_pressed():

def key_down_pressed():

def add_new_number():
    global numbers
    y=random.randrange(4)
    x=random.randrange(4)
    if (numbers[y][x] == 0):
        numbers[y][x] = 2
    else:
        add_new_number()

# numbers = [[1,2,3,4],[5,6,7,8],[1,22,333,4444],[1111,2222,3333,4444]]
numbers = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]


while True:
    y = 1
    x = 1
    ch = win.getch()
    for y in range(4):
        for x in range(4):
            win.addstr(1+y*2,1+x*5,str(numbers[y][x]))

    if ch == curses.KEY_LEFT:
        key_left_pressed():
        add_new_number()
    if ch == curses.KEY_RIGHT:
        key_right_pressed():
        add_new_number()
    if ch == curses.KEY_UP:
        key_up_pressed():
        add_new_number()
    if ch == curses.KEY_DOWN:
        key_down_pressed():
        add_new_number()

    if ch == 27:
        break

curses.endwin()
