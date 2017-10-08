from charword import charword
from robchar import robchar
import security
import json, random, curses, time



def forChar(length, listName, listRow):
    for loops in range(length):
        listName[listRow].append(robchar(charRand(), None))

def charRand():
    charList = ['#','|','$','!','+',';','/','*','^','=',]
    return charList[random.randint(0,9)]

def cursesprinter(stdscr, arrayname):
    line = 7 # print each addstr on a new lne
    for loops in range(5):
        looper = 0 # column to print character at
        for xloop in range(24):
            stdscr.addstr(line,looper+10,str(arrayname[loops][xloop]),curses.color_pair(1))
            looper +=2
        line += 1

def game(stdscr, level):

    # edit make a box 
    global screen
    screen = stdscr.subwin(25, 80, 0, 0)
    screen.box()
    screen.refresh()

    def wordGetter():
        """ Gets words from a list, returning them
        easy (5 letters, 3 words), 
        medium (7 letters, 5 words),
        hard (9 letters, 7 words) """
        nonlocal level
        with open('words.json') as words_:
            word_data = json.load(words_)
        
        wrdSet = random.randint(0,3)

        if level == "easy":
            return(word_data["Easy"][wrdSet])
        elif level == "medium":
            return(word_data["Medium"][wrdSet])
        elif level == "hard":
            return(word_data["Hard"][wrdSet])


    """ GAMES START HERE """
    wordList = wordGetter()
    
    gameAry = [[],[],[],[],[]]
    for loops in range(5):
        forChar(24,gameAry,loops)
            
    stdscr.clear()
    security.showcontrols(stdscr, "turnoff")

    cursesprinter(stdscr, gameAry)

    row = 0
    column = 0
    selected = False
    while True:
        screen.box()
        m = stdscr.getch()
        if m == ord('q') or m == ord('Q'): # quit
            stdscr.clear()
            screen.box()
            stdscr.addstr(5,30,"Please Try Again Later!",curses.color_pair(1))
            stdscr.refresh()
            security.noise('gamelose')
            time.sleep(1)
            stdscr.clear()
            break
        elif m == ord('w') or m == ord('W') or m == curses.KEY_UP:
            row -= 1
            if row < 0:
                row = 4
        elif m == ord('s') or m == ord('S') or m == curses.KEY_DOWN:
            row += 1
            if row > 4:
                row = 0
        elif m == ord('a') or m == ord('A') or m == curses.KEY_LEFT:
            column -= 1
            if column < 0:
                column = 23
        elif m == ord('d') or m == ord('D') or m == curses.KEY_RIGHT:
            column += 1
            if column > 23:
                column = 0
        elif m == curses.KEY_ENTER or m == 10 or m == 13 or m == ord('e'):
            if row != 0:
                security.noise('select')
                selected = True
        
        if selected == False:
            security.noise('keys')

        stdscr.addstr(1,1," " +gameAry[row][column].string()+ " ",curses.color_pair(2))

###



