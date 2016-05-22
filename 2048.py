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

numbers = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
#following line makes testing easier for game over: comment out the numbers list filled with zeros and use the following numbers variable instead.
# numbers = [[1,3,5,7],[9,11,13,15],[17,19,21,23],[25,0,0,0]]

status=1 #status variable tracks if moving or addition actions were successfully made after a new number was added

def move_left(x): #modified bubble sorting algorithm that moves all the zeros to the right place
    global numbers
    global status
    global valid_move
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
                status=1
                valid_move=0
            else:
                if valid_move==0:
                    valid_move=valid_move+1
        passnum = passnum-1

def move_up(y): #modified bubble sorting algorithm that moves all the zeros to the right place
    global numbers
    global status
    global valid_move
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
                status=1
                valid_move=0
            else:
                if valid_move==1:
                    valid_move=valid_move+1
        passnum = passnum-1

def move_right(x): #modified bubble sorting algorithm that moves all the zeros to the right place
    global numbers
    global status
    global valid_move
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
                status=1
                valid_move=0
            else:
                if valid_move==2:
                    valid_move=valid_move+1
        passnum = passnum-1

def move_down(y): #modified bubble sorting algorithm that moves all the zeros to the right place
    global numbers
    global status
    global valid_move
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
                status=1
                valid_move=0
            else:
                if valid_move==3:
                    valid_move=valid_move+1
        passnum = passnum-1

def add_left(x): #if two numbers are of the same value next to each other in the plane of the pressed key, this function multiplies one of them by 2 and makes the other number a zero.
    global numbers
    global status
    global valid_move
    for i in range(3):
        if numbers[x][i]==numbers[x][i+1] and numbers[x][i]!=0:
            numbers[x][i+1]=numbers[x][i+1]*2
            numbers[x][i]=0
            status=1
            valid_move=0
        else:
            if valid_move==0:
                valid_move=valid_move+1

def add_up(y): #if two numbers are of the same value next to each other in the plane of the pressed key, this function multiplies one of them by 2 and makes the other number a zero.
    global numbers
    global status
    global valid_move
    for i in range(3):
        if numbers[i][y]==numbers[i+1][y] and numbers[i][y]!=0:
            numbers[i+1][y]=numbers[i+1][y]*2
            numbers[i][y]=0
            status=1
            valid_move=0
        else:
            if valid_move==1:
                valid_move=valid_move+1

def add_right(x): #if two numbers are of the same value next to each other in the plane of the pressed key, this function multiplies one of them by 2 and makes the other number a zero.
    global numbers
    global status
    global valid_move
    for i in reversed(range(3)):
        if numbers[x][i]==numbers[x][i+1] and numbers[x][i+1]!=0:
            numbers[x][i]=numbers[x][i]*2
            numbers[x][i+1]=0
            status=1
            valid_move=0
        else:
            if valid_move==2:
                valid_move=valid_move+1

def add_down(y): #if two numbers are of the same value next to each other in the plane of the pressed key, this function multiplies one of them by 2 and makes the other number a zero.
    global numbers
    global status
    global valid_move
    for i in reversed(range(3)):
        if numbers[i][y]==numbers[i+1][y] and numbers[i][y]!=0:
            numbers[i][y]=numbers[i][y]*2
            numbers[i+1][y]=0
            status=1
            valid_move=0
        else:
            if valid_move==3:
                valid_move=valid_move+1


def key_left_pressed(): #what happens when the given key is pressed
    global status
    for x in range(4):
        move_left(x)
        add_left(x)
        move_left(x)
    add_new_number()

def key_right_pressed(): #what happens when the given key is pressed
    global status
    for x in range(4):
        move_right(x)
        add_right(x)
        move_right(x)
    add_new_number()

def key_up_pressed(): #what happens when the given key is pressed
    global status
    for y in range(4):
        move_up(y)
        add_up(y)
        move_up(y)
    add_new_number()

def key_down_pressed(): #what happens when the given key is pressed
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
    y=random.randrange(4) #- These two generate a random coordinate for the new numebr to be added.
    x=random.randrange(4) #/

    if numbers[y][x] == 0 and status==1:
        two_or_four = random.randrange(10)
        if two_or_four !=1:
            numbers[y][x] = 2
        else:
            numbers[y][x] = 4 #with a 10% chance of adding a 4
        status=0
        valid_move=0
        highest=max(numbers)
        win.addstr(10,5,"                   ")


    elif status==1:
        add_new_number()
        win.addstr(10,5,"                   ")
    else:
        status=2
        if status==2:
            win.addstr(10,5,"Try other direction")

add_new_number()
win.addstr(10,5,"Press ESC to quit")
while True:

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

    if valid_move==4:
        win.addstr(10,5,"                   ")
        win.addstr(10,5,"Game over!")

    if ch == 27:
        break

curses.endwin()
