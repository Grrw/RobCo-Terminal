import random, json, time, datetime, curses

def t():
    length = random.randrange(0,5)
    length = "0." + str(length)
    time.sleep(float(length))

def startup(stdscr):
    now = datetime.datetime.now()
    length = random.randrange(30021, 68904, 7)
    stdscr.clear()
    stdscr.refresh()

    stdscr.addstr(' **** ROBCO TERMLINK UPLINK SYSTEM ****\n',curses.color_pair(1))
    stdscr.refresh()
    stdscr.addstr('       '+str(now)+'\n',curses.color_pair(1))
    stdscr.refresh()
    startupList = [
        ' RobCo-OS v7.6.0.3\n',
        ' SYSTEM 64k RAM\n',
        ' NO HOLOTAPE FOUND\n',
        ' 00b160ff 00064b72 0005aa6c 000a36c0 0007dc12 0007d490 00018471 000b16d3\n',
        ' load 7a 73 6e 74 6c\n',
        ' '+str(length)+' BYTES FREE | OK\n',
        ' 120 POKE 736, ' + str(length) + ' x$=""LH) 6;T\n',
        ' unable to resolve host TERML-z' + str(length)+'\n',
        ' Get: 2 14kbps [472 B]\n'
        ' No UNIVAC tape found. Mounted drive in /mnt/.\n',
        ' Processor: GE Athlon(tm) 16 Processor 10+\n'
        ' Memory Testing: '+str(length)+'(Installed:8984)\n',
        ' ASN ABN-SLI energy ACPI rev 1011-010\n',
        ' '+str(now)+'\n',
        ' Temperature: '+str(length)+'°Ra\n',
        ' Temperature protection is ON\n',
        ' CPU SPEED '+str(length)+'9172 Hz\n',
        ' No Audio Chip Found. Onboard Audio Disabled.\n',
        ' K987PV-PLUS-PRO\n',
        ' RobCo Macrosystems 6e UNABLE-5 10-\n',
        ' No Virtual Machine support found.\n',
        ' Virus Support [Disabled]\n',
        ' NetPreceder(tm) Lettering Test: F Ώ Ж 化け � [FAIL]\n'
    ]
    stdscr.addstr(' BOOTING SYSTEM.\n',curses.color_pair(1))
    time.sleep(1.3)
    t()
    for q in range(19):
        item = random.randrange(0, len(startupList))
        stdscr.addstr(startupList[item],curses.color_pair(1))
        stdscr.refresh()
        startupList.pop(item)
        t()
        t()
    stdscr.clear()
    stdscr.refresh()
    length -= 11111
    if length < 10000:
        length = random.randrange(10000, 99999)
    l = str(length)
    stdscr.addstr(' LOAD ROM('+l[2]+l[1]+l[4]+'): TRSPS MNGR V'+l[0]+l[3]+l[2]+'\n\n',curses.color_pair(1))
    stdscr.refresh()
    time.sleep(2.3)
    t()
    stdscr.clear()
    stdscr.refresh()
    stdscr.addstr(' ROBCO INDUSTRIES UNIFIED OPERATING SYSTEM\n',curses.color_pair(1))
    stdscr.refresh()
    t()
    stdscr.addstr('   COPYRIGHT 2075-2077 ROBCO INDUSTRIES\n',curses.color_pair(1))
    stdscr.addstr('        '+str(now)+'\n',curses.color_pair(1))
    stdscr.addstr('\n')
    stdscr.refresh()
    stdscr.addstr(3,18,'[',curses.color_pair(1))
    stdscr.addstr(3,22,']\n',curses.color_pair(1))
    t()
    time.sleep(0.5)
    t()
    stdscr.addstr('   -RobCo Trespasser Management System-\n',curses.color_pair(1))
    stdscr.refresh()
    t()
    stdscr.addstr(5,3,'[',curses.color_pair(1))
    stdscr.addstr(5,38,']',curses.color_pair(1))
    acc = 4
    number = 0
    for x in range(34):
        stdscr.addch(5,acc,ord('='),curses.color_pair(1))
        if number < 10:
            stdscr.addstr(3,19,'0'+str(number)+'%',curses.color_pair(1))
        else:
            stdscr.addstr(3,19,str(number)+'%',curses.color_pair(1))
        
        stdscr.refresh()
        acc += 1
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
        print(user_list[popper])
        user_list.pop(popper)
        t()
        time.sleep(0.2)
    print(chr(27) + "[2J")
    return startupList



def minigamePrint(row, words, val_dict):
    if row == 1:
        pass

    elif row == 2:
        pass
    
    elif row == 3:
        pass