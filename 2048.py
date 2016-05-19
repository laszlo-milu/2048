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

def add_left(x):
    global numbers
    for i in range(3):
        if numbers[x][i]==numbers[x][i+1] and numbers[x][i]!=0:
            numbers[x][i+1]=numbers[x][i+1]*2
            numbers[x][i]=0

def add_up(y):
    global numbers
    for i in range(3):
        if numbers[i][y]==numbers[i+1][y] and numbers[i][y]!=0:
            numbers[i+1][y]=numbers[i+1][y]*2
            numbers[i][y]=0

def add_right(x):
    global numbers
    for i in range(3):
        if numbers[x][i]==numbers[x][i+1] and numbers[x][i+1]!=0:
            numbers[x][i]=numbers[x][i]*2
            numbers[x][i+1]=0

def add_down(y):
    global numbers
    for i in range(3):
        if numbers[i][y]==numbers[i+1][y] and numbers[i][y]!=0:
            numbers[i][y]=numbers[i][y]*2
            numbers[i+1][y]=0


def key_left_pressed():
    for x in range(4):
        bubble_sort_left(x)
        add_left(x)
        bubble_sort_left(x)
    try:
        add_new_number()
    except:
        curses.endwin()
        exit()

def key_right_pressed():
    for x in range(4):
        bubble_sort_right(x)
        add_right(x)
        bubble_sort_right(x)
    try:
        add_new_number()
    except:
        curses.endwin()
        exit()

def key_up_pressed():
    for y in range(4):
        bubble_sort_up(y)
        add_up(y)
        bubble_sort_up(y)
    try:
        add_new_number()
    except:
        curses.endwin()
        exit()

def key_down_pressed():
    for y in range(4):
        bubble_sort_down(y)
        add_down(y)
        bubble_sort_down(y)
    try:
        add_new_number()
    except:
        curses.endwin()
        exit()

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
    # y = 1
    # x = 1
    ch = win.getch()
    for y in range(4):
        for x in range(4):
            win.addstr(1+y*2,1+x*5,"    ")
            win.addstr(1+y*2,1+x*5,str(numbers[y][x]))

    if ch == curses.KEY_LEFT:
        key_left_pressed()

    if ch == curses.KEY_RIGHT:
        key_right_pressed()

    if ch == curses.KEY_UP:
        key_up_pressed()

    if ch == curses.KEY_DOWN:
        key_down_pressed()


    if ch == 27:
        break

curses.endwin()
