import random, json, time, datetime, curses

def noise(kind):
    try:
        import pygame
        pygame.mixer.init()
        if kind == 'poweron':
            song = pygame.mixer.Sound("audio/poweron.ogg")
            pygame.mixer.Sound.play(song)
            time.sleep(0.7)
        elif kind == 'poweroff':
            song = pygame.mixer.Sound("audio/poweroff.ogg")
            pygame.mixer.Sound.play(song)
            time.sleep(0.3)
        elif kind == "keys":
            noise = random.randint(1, 9)
            key = 'audio/' + str(noise) + '.ogg'
            song = pygame.mixer.Sound(key)
            pygame.mixer.Sound.play(song)
        elif kind == 'select':
            song = pygame.mixer.Sound("audio/select.ogg")
            pygame.mixer.Sound.play(song)
    except:
        f = open('noaudio.txt', 'w+')
        f.write('Pygame not installed')

def t():
    length = random.gauss(0.15,0.08)
    time.sleep(max(0, length))

def startup(stdscr):
    now = datetime.datetime.now()
    length = random.randrange(30021, 68904, 7)

    stdscr.clear()
    screen = stdscr.subwin(25, 80, 0, 0)
    screen.box()
    screen.refresh()

    stdscr.addstr(1,21,'**** ROBCO TERMLINK UPLINK SYSTEM ****',curses.color_pair(1))
    stdscr.refresh()
    startupList = [
        'RobCo-OS v7.6.0.3',
        'SYSTEM 64k RAM',
        'NO HOLOTAPE FOUND',
        '00b160ff 00064b72 0005aa6c 000a36c0 0007dc12 0007d490',
        'load 7a 73 6e 74 6c',
         str(length)+' BYTES FREE | OK',
        '120 POKE 736, ' + str(length) + ' x$=""LH) 6;T',
        'unable to resolve host TERML-z' + str(length)+'',
        'Get: 2 14kbps [472 B]'
        'No UNIVAC tape found. Mounted drive in /mnt/.',
        'Processor: GE Athlon(tm) 16 Processor 10+'
        'Memory Testing: '+str(length)+' B (8984 B)',
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
    stdscr.addstr(1,20,'ROBCO INDUSTRIES UNIFIED OPERATING SYSTEM',curses.color_pair(1))
    stdscr.refresh()
    t()
    stdscr.addstr(2,22,'COPYRIGHT 2075-2077 ROBCO INDUSTRIES',curses.color_pair(1))
    stdscr.addstr(3,28,str(now),curses.color_pair(1))
    stdscr.refresh()
    stdscr.addstr(4,37,'[',curses.color_pair(1))
    stdscr.addstr(4,41,']',curses.color_pair(1))
    t()
    time.sleep(0.5)
    t()
    stdscr.addstr(5,22,'-RobCo Trespasser Management System-',curses.color_pair(1))
    stdscr.refresh()
    t()
    stdscr.addstr(6,22,'[',curses.color_pair(1))
    stdscr.addstr(6,57,']',curses.color_pair(1))
    acc = 23
    number = 0
    for x in range(34):
        stdscr.addch(6,acc,ord('='),curses.color_pair(1))
        if number < 10:
            stdscr.addstr(4,38,'0'+str(number)+'%',curses.color_pair(1))
        else:
            stdscr.addstr(4,38,str(number)+'%',curses.color_pair(1))
        
        stdscr.refresh()
        acc += 1
        if acc < 56:
            number += 3
        t()

    t()
    time.sleep(0.8)

def showcontrols(stdscr, onoff):
    controlsmenu = stdscr.subwin(8, 74, 15, 3)
    controlslist = stdscr.subwin(8, 22, 15, 30)
    if onoff == True:
        controlslist.clear()
        controlsmenu.box()
        controlsmenu.addstr(1,1,'esc  F1 F2 F3 F4 F5 F6 F7 F8 F9 F10 F11 F12   psc srl psb',curses.color_pair(1))
        controlsmenu.addstr(2,1,' ~   1  2  3  4  5  6  7  8  9  0 -  = bksp   ins hom pup   nlk /  *  -',curses.color_pair(1))
        controlsmenu.addstr(3,1,' TAB  Q  W  E  R  T  Y  U  I  O  P  [ ]  \\    del end pdn    7  8  9  +',curses.color_pair(1))
        controlsmenu.addstr(4,1,'CAPLK  A  S  D  F  G  H  J  K  L  ;  \' RET                   4  5  6',curses.color_pair(1))
        controlsmenu.addstr(5,1,'SHIFT  Z  X  C  V  B  N  M  ,  .   /  SHIFT        ^         1  2  3 ent',curses.color_pair(1))
        controlsmenu.addstr(6,1,'ctrl win alt |   space    | alt win pn ctrl     <  V  >      0 ins del',curses.color_pair(1))
        controlsmenu.addstr(3,6,' Q  W  E ',curses.color_pair(2))
        controlsmenu.addstr(4,7,' A  S  D ',curses.color_pair(2))
        controlsmenu.addstr(4,40, ' RET ',curses.color_pair(2))
        controlsmenu.addstr(5,51,' ^ ',curses.color_pair(2))
        controlsmenu.addstr(6,48,' <  V  > ',curses.color_pair(2))
    else:
        controlsmenu.clear()
        controlslist.box()
        controlslist.addstr(1,2,'W or ^ ........ up',curses.color_pair(1))
        controlslist.addstr(2,2,'S or V ...... down',curses.color_pair(1))
        controlslist.addstr(3,2,'A or < ...... left',curses.color_pair(1))
        controlslist.addstr(4,2,'D or > ..... right',curses.color_pair(1))
        controlslist.addstr(5,2,'E or RET .. select',curses.color_pair(1))
        controlslist.addstr(6,2,'Q ........... quit',curses.color_pair(1))
    return False