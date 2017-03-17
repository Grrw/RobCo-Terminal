import random, json, time, datetime, curses

def t():
    length = random.gauss(0.15,0.08)
    time.sleep(max(0, length))

def startup(stdscr):
    stdscr.box()
    now = datetime.datetime.now()
    length = random.randrange(30021, 68904, 7)
    stdscr.clear()
    stdscr.refresh()

    screen = stdscr.subwin(25, 100, 0, 0)
    screen.box()
    screen.refresh()

    stdscr.addstr(1,31,'**** ROBCO TERMLINK UPLINK SYSTEM ****',curses.color_pair(1))
    stdscr.refresh()
    startupList = [
        'RobCo-OS v7.6.0.3',
        'SYSTEM 64k RAM',
        'NO HOLOTAPE FOUND',
        '00b160ff 00064b72 0005aa6c 000a36c0 0007dc12 0007d490 00018471 000b16d3',
        'load 7a 73 6e 74 6c',
         str(length)+' BYTES FREE | OK',
        '120 POKE 736, ' + str(length) + ' x$=""LH) 6;T',
        'unable to resolve host TERML-z' + str(length)+'',
        'Get: 2 14kbps [472 B]'
        'No UNIVAC tape found. Mounted drive in /mnt/.',
        'Processor: GE Athlon(tm) 16 Processor 10+'
        'Memory Testing: '+str(length)+' B (Installed:8984 B)',
        'ASN ABN-SLI energy ACPI rev 1011-010',
         str(now)+'',
        'Temperature: '+str(length)+'°Ra',
        'Temperature protection is ON',
        'CPU SPEED '+str(length)+'9172 Hz',
        'No Audio Chip Found. Onboard Audio Disabled.',
        'K987PV-PLUS-PRO',
        'RobCo Macrosystems 6e UNABLE-5 10-',
        'No Virtual Machine support found.',
        'Virus Support [Disabled]',
        'NetPreceder(tm) Lettering Test: F Ώ Ж 化け � [FAIL]'
    ]
    stdscr.addstr(2,1,'BOOTING SYSTEM.',curses.color_pair(1))
    time.sleep(1.3)
    t()
    rand_s_acc = 3
    for q in range(18):
        item = random.randrange(0, len(startupList))
        stdscr.addstr(rand_s_acc,1,startupList[item],curses.color_pair(1))
        rand_s_acc += 1
        stdscr.refresh()
        startupList.pop(item)
        t()
        t()
    stdscr.clear()
    screen.box()
    stdscr.refresh()
    length -= 11111
    if length < 10000:
        length = random.randrange(10000, 99999)
    l = str(length)
    stdscr.addstr(1,1,'LOAD ROM('+l[2]+l[1]+l[4]+'): TRSPS MNGR V'+l[0]+l[3]+l[2]+'',curses.color_pair(1))
    stdscr.refresh()
    time.sleep(2.3)
    t()
    stdscr.clear()
    screen.box()
    stdscr.refresh()
    stdscr.addstr(1,29,'ROBCO INDUSTRIES UNIFIED OPERATING SYSTEM',curses.color_pair(1))
    stdscr.refresh()
    t()
    stdscr.addstr(2,31,'COPYRIGHT 2075-2077 ROBCO INDUSTRIES',curses.color_pair(1))
    stdscr.addstr(3,37,str(now),curses.color_pair(1))
    stdscr.refresh()
    stdscr.addstr(4,46,'[',curses.color_pair(1))
    stdscr.addstr(4,50,']',curses.color_pair(1))
    t()
    time.sleep(0.5)
    t()
    stdscr.addstr(5,31,'-RobCo Trespasser Management System-',curses.color_pair(1))
    stdscr.refresh()
    t()
    stdscr.addstr(6,31,'[',curses.color_pair(1))
    stdscr.addstr(6,67,']',curses.color_pair(1))
    acc = 32
    number = 0
    for x in range(35):
        stdscr.addch(6,acc,ord('='),curses.color_pair(1))
        if number < 10:
            stdscr.addstr(4,47,'0'+str(number)+'%',curses.color_pair(1))
        else:
            stdscr.addstr(4,47,str(number)+'%',curses.color_pair(1))
        
        stdscr.refresh()
        acc += 1
        if acc < 66:
            number += 3
        t()

    t()
    time.sleep(0.8)

def showcontrols(stdscr, onoff):
    controlsmenu = stdscr.subwin(8, 74, 15, 2)
    controlslist = stdscr.subwin(9, 22, 14, 76)
    if onoff == True:
        controlsmenu.box()
        controlsmenu.addstr(1,1,'esc  f1 f2 f3 f4 f5 f6 f7 f8 f9 f10 f11 f12   psc srl psb',curses.color_pair(1))
        controlsmenu.addstr(2,1,' ~   1  2  3  4  5  6  7  8  9  0 -  = bksp   ins hom pup   nlk /  *  -',curses.color_pair(1))
        controlsmenu.addstr(3,1,' TAB  q  w  e  r  t  y  u  i  o  p  [ ]  \\    del end pdn    7  8  9  +',curses.color_pair(1))
        controlsmenu.addstr(4,1,'CAPLK  a  s  d  f  g  h  j  k  l  ;  \' RET                  4  5  6',curses.color_pair(1))
        controlsmenu.addstr(5,1,'SHIFT  z  x  c  v  b  n  m  ,  .   /  SHIFT        ^         1  2  3 ent',curses.color_pair(1))
        controlsmenu.addstr(6,1,'ctrl win alt |   space    | alt win pn ctrl     <  V  >      0 ins del',curses.color_pair(1))
        controlsmenu.addstr(3,6,' q  w  e ',curses.color_pair(2))
        controlsmenu.addstr(4,7,' a  s  d ',curses.color_pair(2))
        controlsmenu.addstr(4,40, ' RET ',curses.color_pair(2))
        controlsmenu.addstr(5,51,' ^ ',curses.color_pair(2))
        controlsmenu.addstr(6,48,' <  V  > ',curses.color_pair(2))
        controlslist.box()
        controlslist.addstr(1,6,' CONTROLS ',curses.color_pair(2))
        controlslist.addstr(2,2,'w or ^ ........ up',curses.color_pair(1))
        controlslist.addstr(3,2,'s or V ...... down',curses.color_pair(1))
        controlslist.addstr(4,2,'a or < ...... left',curses.color_pair(1))
        controlslist.addstr(5,2,'d or > ..... right',curses.color_pair(1))
        controlslist.addstr(6,2,'e or RET .. select',curses.color_pair(1))
        controlslist.addstr(7,2,'q ........... quit',curses.color_pair(1))
    else:
        controlsmenu.clear()
        controlslist.clear()
    return False

def wordGetter(level):
    """
    Gets words from a list, returning them
    levels are: easy (5 letters), medium (7 letters), hard (9 letters)
    """
    with open('words.json') as words_:
        word_data = json.load(words_)
    if level == "easy":
        return(word_data["Easy"])
    elif level == "medium":
        return(word_data["Medium"])
    elif level == "hard":
        return(word_data["Hard"])

def initrand(user_list):
    """
    Takes words from the list, returning 5 random words
    """
    startupList = []
    for x in range(5):
        popper = random.randrange(0, len(user_list))
        startupList.append(user_list[popper])
        user_list.pop(popper)
        t()
        time.sleep(0.2)
    return startupList