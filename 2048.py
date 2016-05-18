import curses
screen = curses.initscr()
curses.noecho()
curses.curs_set(0)
win = curses.newwin(curses.LINES, curses.COLS, 0, 0)
win.keypad(1)
win.border(0)
win.nodelay(1)

#numbers = [[1,2,3,4],[5,6,7,8],[1,22,333,4444],[1111,2222,3333,4444]]
numbers = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
while True:
    y = 1
    x = 1
    ch = win.getch()
    for y in range(4):
        for x in range(4):
            win.addstr(1+y*2,1+x*5,str(numbers[y][x]))

    '''win.addstr(y,x,str(numbers[0][0]))
    win.addstr(y,x+5,str(numbers[0][1]))
    win.addstr(y,x+10,str(numbers[0][2]))
    win.addstr(y,x+15,str(numbers[0][3]))

    win.addstr(y+2,x,str(numbers[1][0]))
    win.addstr(y+2,x+5,str(numbers[1][1]))
    win.addstr(y+2,x+10,str(numbers[1][2]))
    win.addstr(y+2,x+15,str(numbers[1][3]))

    win.addstr(y+4,x,str(numbers[2][0]))
    win.addstr(y+4,x+5,str(numbers[2][1]))
    win.addstr(y+4,x+10,str(numbers[2][2]))
    win.addstr(y+4,x+15,str(numbers[2][3]))

    win.addstr(y+6,x,str(numbers[3][0]))
    win.addstr(y+6,x+5,str(numbers[3][1]))
    win.addstr(y+6,x+10,str(numbers[3][2]))
    win.addstr(y+6,x+15,str(numbers[3][3]))'''

    win.refresh()
    if ch == 27:
        break

curses.endwin()
