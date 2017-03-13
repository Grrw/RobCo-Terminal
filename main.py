import security
import getch, time, datetime

security.startup()

quit_ = False
while not quit_:
    selector = False
    secondarySelector= True
    aa=ba=ca=da='  '
    row = 0
    selected = False
    # main menu selection
    while not selector: 
        rowFour = False

        print(chr(27) + "[2J")
        now = datetime.datetime.now()
        print(' ROBCO INDUSTRIES UNIFIED OPERATING SYSTEM')
        print('   COPYRIGHT 2075-2077 ROBCO INDUSTRIES')
        print('        '+str(now)+'\n')
        print('   -RobCo Trespasser Management System-')
        print('   ====================================')
        print()
        print('               ',aa,'Easy',aa)
        print('              ',ba,'Medium',ba)
        print('               ',ca,'Hard',ca)
        print('              ',da,'Reboot',da)

        m = getch.getch()
        # 'w' and 's' work "upside down", because w moves up visually and down in row number, and s is vice versa
        if m == 'q':
            selector = True
            quit_ = True
        elif m == 'w':
            row = row - 1
            if row <= 0:
                row = 4
        elif m == 's':
            row = row + 1
            if row >= 5:
                row = 1
        elif m == '\n':
            if row != 0:
                selected = True
            pass
        #every press but return will move the "cursor"
        if selected != True:
            aa=ba=ca=da='  '
            if row == 1:
                aa = '▐▌'
            elif row == 2:
                ba = '▐▌'
            elif row == 3:
                ca = '▐▌'
            elif row == 4:
                da = '▐▌'
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

    while not secondarySelector: 

        print(chr(27) + "[2J")

        m = getch.getch()
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
