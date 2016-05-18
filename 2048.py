import curses
screen = curses.initscr()
curses.noecho()
curses.curs_set(0)
win = curses.newwin(curses.LINES, curses.COLS, 0, 0)
win.keypad(1)
win.border(0)
win.nodelay(1)
import random

def add_new_number():
    global numbers
    y=random.randrange(4)
    x=random.randrange(4)
    if (numbers[y][x] == 0):
        numbers[y][x] = 2
    else:
        add_new_number()

#numbers = [[1,2,3,4],[5,6,7,8],[1,22,333,4444],[1111,2222,3333,4444]]
numbers = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]


while True:
    y = 1
    x = 1
    ch = win.getch()
    for y in range(4):
        for x in range(4):
            win.addstr(1+y*2,1+x*5,str(numbers[y][x]))

    # win.refresh()
    if ch == 32:
        add_new_number()
    if ch == 27:
        break

curses.endwin()
