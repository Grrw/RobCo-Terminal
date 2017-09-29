import security, time, os
def c():
    os.system('cls' if os == 'nt' else 'clear')
    print('security.noise() audio test!\nType the sound you want to play then press return')
    print("Type 'displaysounds' to display all audio options\n")
while True:
    c()
    m = input('> ')
    if m =='displaysounds':
        list_ = os.listdir('audio')[1:]
        list_.append('secretboot....')
        c()
        for x in list_:
            print(x[:-4])
        input("\nPress return to continue")
    if m =='secretboot':
        security.noise('boot')
        security.noise('hgboot')
    else:
        security.noise(m)