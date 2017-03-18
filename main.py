"""
Main Window Size: 25 rows by 100 columns
'Keyboard' Window Size: 8, 74, 15, 2
'Controls' Windoe Size: 9, 22, 14, 76
"""

import security
import curses, time, datetime, os, sys
from curses import wrapper

def clears(stdscr): # clear and re-box the screen
    stdscr.clear()
    screen.box()
    stdscr.refresh()

def mainwindow(stdscr): # print the main menu window
    now = datetime.datetime.now()
    stdscr.addstr(1,29,'ROBCO INDUSTRIES UNIFIED OPERATING SYSTEM',curses.color_pair(1))
    stdscr.addstr(2,31,'COPYRIGHT 2075-2077 ROBCO INDUSTRIES',curses.color_pair(1))
    stdscr.addstr(3,37,str(now),curses.color_pair(1))
    stdscr.addstr(4,42,'Press Q to Quit',curses.color_pair(1))
    stdscr.addstr(5,31,'-RobCo Trespasser Management System-',curses.color_pair(1))
    stdscr.addstr(6,31,'[===================================]',curses.color_pair(1))
    stdscr.addstr(7,47,' Easy ',curses.color_pair(1))
    stdscr.addstr(8,46,' Medium ',curses.color_pair(1))
    stdscr.addstr(9,47,' Hard ',curses.color_pair(1))
    stdscr.addstr(10,46,' Reboot ',curses.color_pair(1))
    stdscr.addstr(11,45,' Controls ',curses.color_pair(1))

def gameWindow(stdscr):
    # one function won't cut it, probably make a class
    pass

# first thing to run, make sure that the terminal window is minimum size or more
rows, columns = os.popen('stty size', 'r').read().split()
if int(rows) < 25 or int(columns) < 100:
    print('Your terminal window is: '+rows+' rows by '+columns+' columns')
    print('Please resize to greater than 25 rows by 100 columns')
    print('Press Return to continue')
    input()
    sys.exit()

# initiate curses scr
stdscr = curses.initscr()

def main(stdscr):
    """
    Main non-function part of the code in a function so that the
    curses wrapper can prevent a terminal from staying in curses
    mode in the event of an error.
    Even ^C would normally bugger the terminal
    """

    # configure curses settings
    curses.start_color()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)

    # edit make a box 
    global screen
    screen = stdscr.subwin(25, 100, 0, 0)
    screen.box()
    screen.refresh()

    """
    Turn on startup when done testing
    security.startup(stdscr)
    """

    quit_ = False # main loop
    while not quit_:
        selector = False # primary loop (main menu)
        secondarySelector= True # secondary loop (actual game)
        row = 0 # internally store what is highlighted on the Y axis
        colum = 0 # internally store what is highlighted on the X axis
        selected = False # if return is hit, use row number to pass difficulty
        skipper = False # used for skipping the difficulty selection in primary loop
        # row'x' is used to decide which non-difficulty option the user selected
        rowFour = False # reboot
        rowFive = True # controls

        clears(stdscr)
        mainwindow(stdscr)

        # main menu selection
        while not selector: 
            rowFour = False
            selected = False

            skipper = security.showcontrols(stdscr, rowFive)
            # showcontrols always returns False

            m = stdscr.getch()
            # 'w' and 's' move the selection in their respective arrow keys
            if m == ord('q'): # quit
                selector = True
                quit_ = True
            elif m == ord('w') or m == curses.KEY_UP:
                row = row - 1
                if row <= 0:
                    row = 5
            elif m == ord('s') or m == curses.KEY_DOWN:
                row = row + 1
                if row >= 6:
                    row = 1
            elif m == curses.KEY_ENTER or m == 10 or m == 13 or m == ord('e'):
                if row != 0:
                    selected = True
                pass

            if selected != True:
                mainwindow(stdscr)
                if row == 1:
                    stdscr.addstr(7,47,' Easy ', curses.color_pair(2))
                elif row == 2:
                    stdscr.addstr(8,46,' Medium ', curses.color_pair(2))
                elif row == 3:
                    stdscr.addstr(9,47,' Hard ', curses.color_pair(2))
                elif row == 4:
                    stdscr.addstr(10,46,' Reboot ', curses.color_pair(2))
                elif row == 5:
                    stdscr.addstr(11,45,' Controls ',curses.color_pair(2))

            else:
                if row == 4:
                    rowFour = True
                    skipper = True
                elif row == 5:
                    # switch rowFive to allow toggling of the controls
                    if rowFive == False:
                        rowFive = True
                    elif rowFive == True:
                        rowFive = False
                    skipper = True
                else:
                    rowFour == False
                if row == 1:
                    difficulty = security.wordGetter('easy')
                elif row == 2:
                    difficulty = security.wordGetter('medium')
                elif row == 3:
                    difficulty = security.wordGetter('hard')

                if skipper == False:
                    difficulty = security.initrand(difficulty) # get a new dictionary of 5 words instead of 13
                    selector = True
                    secondarySelector = False
                elif rowFour == True:
                    clears(stdscr)
                    time.sleep(1)
                    security.t()
                    rowFive = True
                    security.startup(stdscr)
                    mainwindow(stdscr)
                else:
                    pass

        while not secondarySelector: 

            clears(stdscr)

            m = stdscr.getch()
            if m == ord('q'):
                secondarySelector = True
            elif m == 'w':
                print('up')
            elif m == 's':
                print('down')
            elif m == 'a':
                print('left')
            elif m == 'd':
                print('right')
            elif m == '\n':
                print('return')

    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

wrapper(main)


