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
    stdscr.addstr(1,30,'ROBCO INDUSTRIES UNIFIED OPERATING SYSTEM',curses.color_pair(1))
    stdscr.refresh()
    t()
    stdscr.addstr(2,32,'COPYRIGHT 2075-2077 ROBCO INDUSTRIES',curses.color_pair(1))
    stdscr.addstr(3,37,str(now),curses.color_pair(1))
    stdscr.refresh()
    stdscr.addstr(4,47,'[',curses.color_pair(1))
    stdscr.addstr(4,51,']',curses.color_pair(1))
    t()
    time.sleep(0.5)
    t()
    stdscr.addstr(5,32,'-RobCo Trespasser Management System-',curses.color_pair(1))
    stdscr.refresh()
    t()
    stdscr.addstr(6,32,'[',curses.color_pair(1))
    stdscr.addstr(6,68,']',curses.color_pair(1))
    acc = 33
    number = 0
    for x in range(35):
        stdscr.addch(6,acc,ord('='),curses.color_pair(1))
        if number < 10:
            stdscr.addstr(4,48,'0'+str(number)+'%',curses.color_pair(1))
        else:
            stdscr.addstr(4,48,str(number)+'%',curses.color_pair(1))
        
        stdscr.refresh()
        acc += 1
        if acc < 67:
            number += 3
        t()

    t()
    time.sleep(0.8)

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



def minigamePrint(row, words, val_dict):
    if row == 1:
        pass

    elif row == 2:
        pass
    
    elif row == 3:
        pass