import security
import getch, time, datetime

security.startup()

quit_ = False
while not quit_:
    selector = False
    secondarySelector= True
    aa=ba=ca='  '
    row = 0
    selected = False
    # main menu selection
    while not selector: 

        print(chr(27) + "[2J")
        now = datetime.datetime.now()
        print(' ROBCO INDUSTRIES UNIFIED OPERATING SYSTEM')
        print('   COPYRIGHT 2075-2077 ROBCO INDUSTRIES')
        print('        '+str(now)+'\n')
        print('   -RobCo Trespasser Management System-')
        print('   ====================================')
        print()
        print('               ',aa,'Easy',aa, '              ') #easy hacking
        print('              ',ba,'Medium',ba, '              ') # medium level hacking
        print('               ',ca,'Hard',ca, '              ') # RobCo patented hard-mode hacking

        m = getch.getch()
        # 'w' and 's' work "upside down", because w moves up visually and down in row number, and s is vice versa
        if m == 'q':
            selector = True
            quit_ = True
        elif m == 'w':
            row = row - 1
            if row <= 0:
                row = 3
        elif m == 's':
            row = row + 1
            if row >= 4:
                row = 1
        elif m == '\n':
            if row != 0:
                selected = True
            pass
        #every press but return will move the "cursor"
        if selected != True:
            aa=ba=ca='  '
            if row == 1:
                aa = '▐▌'
            elif row == 2:
                ba = '▐▌'
            elif row == 3:
                ca = '▐▌'
            else:
                pass
        else:
            if row == 1:
                difficulty = security.wordGetter('easy')
            elif row == 2:
                difficulty = security.wordGetter('medium')
            elif row == 3:
                difficulty = security.wordGetter('hard')
            difficulty = security.initrand(difficulty) # get a new dictionary of 5 words instead of 13
            selector = True
            secondarySelector = False

    while not secondarySelector: 

        print(chr(27) + "[2J")

        print(row, difficulty)

        m = getch.getch()
        if m == 'q':
            secondarySelector = True
            quit_ = True
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
