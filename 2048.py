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

def bubble_sort_left(x):
    global numbers
    exchanges = True
    passnum = len(numbers)-1
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):
           if numbers[x][i]<numbers[x][i+1] and numbers[x][i]==0:
               exchanges = True
               temp = numbers[x][i]
               numbers[x][i] = numbers[x][i+1]
               numbers[x][i+1] = temp
       passnum = passnum-1

def bubble_sort_up(y):
    global numbers
    exchanges = True
    passnum = len(numbers)-1
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):
           if numbers[i][y]<numbers[i+1][y] and numbers[i][y]==0:
               exchanges = True
               temp = numbers[i][y]
               numbers[i][y] = numbers[i+1][y]
               numbers[i+1][y] = temp
       passnum = passnum-1

def bubble_sort_right(x):
    global numbers
    exchanges = True
    passnum = len(numbers)-1
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):
           if numbers[x][i]>numbers[x][i+1] and numbers[x][i+1]==0:
               exchanges = True
               temp = numbers[x][i]
               numbers[x][i] = numbers[x][i+1]
               numbers[x][i+1] = temp
       passnum = passnum-1

def bubble_sort_down(y):
    global numbers
    exchanges = True
    passnum = len(numbers)-1
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):
           if numbers[i][y]>numbers[i+1][y] and numbers[i+1][y]==0:
               exchanges = True
               temp = numbers[i][y]
               numbers[i][y] = numbers[i+1][y]
               numbers[i+1][y] = temp
       passnum = passnum-1

# def add_left(x):
#     global numbers
#


def key_left_pressed():

    for x in range(4):
        bubble_sort_left(x)

def key_right_pressed():

    for x in range(4):
        bubble_sort_right(x)

def key_up_pressed():
    for y in range(4):
        bubble_sort_up(y)

def key_down_pressed():
    for y in range(4):
        bubble_sort_down(y)

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
        key_left_pressed()
        add_new_number()
    if ch == curses.KEY_RIGHT:
        key_right_pressed()
        add_new_number()
    if ch == curses.KEY_UP:
        key_up_pressed()
        add_new_number()
    if ch == curses.KEY_DOWN:
        key_down_pressed()
        add_new_number()

    if ch == 27:
        break

curses.endwin()
