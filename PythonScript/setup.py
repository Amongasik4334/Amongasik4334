# ━━━━━━━━━━━━━━━
#C:\Users\Пользователь\PArseKrypto\main.py

import os, sys, time
from colorama import Fore, Back, Style, init

init()

AskLogo = open('scr/Logo.txt', 'r').read().split('/')[0]
SetLogo = open('scr/Logo.txt', 'r').read().split('/')[1]

def Setup():
    print(f'{Style.BRIGHT + SetLogo}\n')
    input('Press Enter for Start Setup')
    main = open('main.py', 'w+')
    print(f'{Fore.RED}##{Fore.WHITE}---')
    print(f'{Fore.YELLOW}####{Fore.WHITE}-')
    print(f'{Fore.GREEN}#####{Fore.WHITE}')
    input()
    main.write(open('scr/setup.config', 'r').read())
    main.close()

Setup()
