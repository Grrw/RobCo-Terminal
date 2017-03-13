import random, json, time, datetime, sys

def t():
    length = random.randrange(0,5)
    length = "0." + str(length)
    time.sleep(float(length))

def onebyone(user_input):
    for x in user_input:
        sys.stdout.write(x)
        sys.stdout.flush()
        t()
    

def startup():
    now = datetime.datetime.now()
    length = random.randrange(30021, 68904, 7)
    print(chr(27) + "[2J")
    print(' **** ROBCO TERMLINK UPLINK SYSTEM ****')
    print('       '+str(now))
    print()
    startupList = [
        ' RobCo-OS v7.6.0.3',
        ' SYSTEM 64k RAM',
        ' NO HOLOTAPE FOUND',
        ' 00b160ff 00064b72 0005aa6c 000a36c0 0007dc12 0007d490 00018471 000b16d3',
        ' load 7a 73 6e 74 6c',
        ' '+str(length)+' BYTES FREE | OK',
        ' 120 POKE 736, ' + str(length) + ' x$=""LH) 6;T',
        ' unable to resolve host TERML-z' + str(length),
        ' Get: 2 14kbps [472 B]'
        ' Init97',
        ' No UNIVAC tape found. Mounted drive in /mnt/.',
        ' Processor: GE Athlon(tm) 16 Processor 10+'
        ' Memory Testing: '+str(length)+'(Installed:8984)',
        ' ASN ABN-SLI energy ACPI rev 1011-010',
        ' '+str(now),
        ' Temperature: '+str(length)+'°Ra',
        ' Temperature protection is ON',
        ' CPU SPEED '+str(length)+'9172 Hz',
        ' No Audio Chip Found. Onboard Audio Disabled.',
        ' K987PV-PLUS-PRO',
        ' RobCo Macrosystems 6e UNABLE-5 10-',
        ' No Virtual Machine support found.',
        ' Virus Support [Disabled]',
        ' NetPreceder(tm) Lettering Test: F Ώ Ж 化け � [FAIL]'
    ]
    print(' BOOTING SYSTEM.')
    time.sleep(1.3)
    t()
    for q in range(random.randrange(11,22)):
        item = random.randrange(0, len(startupList))
        print(startupList[item])
        startupList.pop(item)
        t()
        t()
    length -= 11111
    if length < 10000:
        length = random.randrange(10000, 99999)
    l = str(length)
    print('\n LOAD ROM('+l[2]+l[1]+l[4]+'): TRSPS MNGR V'+l[0]+l[3]+l[2]+'\n')
    time.sleep(2.3)
    t()
    print(' ROBCO INDUSTRIES UNIFIED OPERATING SYSTEM')
    t()
    print('   COPYRIGHT 2075-2077 ROBCO INDUSTRIES')
    print('        '+str(now)+'\n                [Loading]')
    t()
    time.sleep(0.5)
    t()
    print('   -RobCo Trespasser Management System-')
    t()
    onebyone('   ====================================\n')
    t()
    print('')
    t()
    print()
    print()
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