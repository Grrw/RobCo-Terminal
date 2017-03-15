import security
import curses, time, datetime, os, sys
from curses import wrapper

rows, columns = os.popen('stty size', 'r').read().split()
if int(rows) < 25 or int(columns) < 100:
    print('Your terminal window is: '+rows+' rows by '+columns+' columns')
    print('Please resize to greater than 25 rows by 100 columns')
    print('Press Return to continue')
    input()
    sys.exit()

stdscr = curses.initscr()


def main(stdscr):

    curses.start_color()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)

    global screen
    screen = stdscr.subwin(25, 100, 0, 0)
    screen.box()
    screen.refresh()

    security.startup(stdscr)

    quit_ = False
    while not quit_:
        selector = False
        secondarySelector= True
        row = 0
        selected = False

        stdscr.clear()
        stdscr.refresh()
        now = datetime.datetime.now()
        stdscr.move(0,0)
        stdscr.addstr(0,1,'ROBCO INDUSTRIES UNIFIED OPERATING SYSTEM\n',curses.color_pair(1))
        stdscr.addstr(1,3,'COPYRIGHT 2075-2077 ROBCO INDUSTRIES\n',curses.color_pair(1))
        stdscr.addstr(2,8,str(now)+'\n',curses.color_pair(1))
        stdscr.addstr(3,13,'Press Q to Quit',curses.color_pair(1))
        stdscr.addstr(4,3,'-RobCo Trespasser Management System-\n',curses.color_pair(1))
        stdscr.addstr(5,2,'[====================================]\n',curses.color_pair(1))
        stdscr.addstr(6,17,' Easy \n',curses.color_pair(1))
        stdscr.addstr(7,16,' Medium \n',curses.color_pair(1))
        stdscr.addstr(8,17,' Hard \n',curses.color_pair(1))
        stdscr.addstr(9,16,' Reboot ',curses.color_pair(1))
        stdscr.move(9,0)

        # main menu selection
        while not selector: 
            rowFour = False

            m = stdscr.getch()
            # 'w' and 's' work "upside down", because w moves up visually and down in row number, and s is vice versa
            if m == ord('q'):
                selector = True
                quit_ = True
            elif m == ord('w'):
                row = row - 1
                if row <= 0:
                    row = 4
            elif m == ord('s'):
                row = row + 1
                if row >= 5:
                    row = 1
            elif m == curses.KEY_ENTER or m == ord('e'):
                if row != 0:
                    selected = True
                pass
            #every press but return will move the "cursor"
            if selected != True:
                stdscr.addstr(6,17,' Easy \n',curses.color_pair(1))
                stdscr.addstr(7,16,' Medium \n',curses.color_pair(1))
                stdscr.addstr(8,17,' Hard \n',curses.color_pair(1))
                stdscr.addstr(9,16,' Reboot ',curses.color_pair(1))
                if row == 1:
                    stdscr.addstr(6,17,' Easy \n', curses.color_pair(2))
                elif row == 2:
                    stdscr.addstr(7,16,' Medium \n', curses.color_pair(2))
                elif row == 3:
                    stdscr.addstr(8,17,' Hard \n', curses.color_pair(2))
                elif row == 4:
                    stdscr.addstr(9,16,' Reboot \n', curses.color_pair(2))
            else:
                if row == 4:
                    rowFour = True
                    selected = False
                elif row == 1:
                    difficulty = security.wordGetter('easy')
                elif row == 2:
                    difficulty = security.wordGetter('medium')
                elif row == 3:
                    difficulty = security.wordGetter('hard')

                if rowFour == False:
                    difficulty = security.initrand(difficulty) # get a new dictionary of 5 words instead of 13
                    selector = True
                    secondarySelector = False
                    print(difficulty[0]+' '+difficulty[1]+' '+difficulty[2]+' '+difficulty[3]+' '+difficulty[4])
                    time.sleep(1)
                else:
                    print(chr(27) + "[2J")
                    time.sleep(2)
                    security.t()
                    security.startup()
                    rowFour = False

        while not secondarySelector: 

            stdscr.clear

            m = stdscr.getch()
            if m == 'q':
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


