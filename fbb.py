from os import system as c
import os
import time
import random

A = '\033[1;97m'
R = '\033[1;31m'
Y = '\033[1;33m'
G = '\033[1;32m'
C = '\033[1;36m'

def logo():
    c('clear')
    print(f"""{G}
█▀█ █ █▄░█ █▀▀ █ █▄░█
█▀▄ █ █░▀█ █▀░ █ █░▀█
   {Y}FACEBOOK OLD ID HACK TOOL (ROOT ONLY)
{A}-----------------------------------
""")

def check_root():
    if os.geteuid() != 0:
        print(f"\n{R}[!] Root Permission Not Granted!")
        print(f"{Y}[!] This Tool Only Works On Rooted Devices!\n")
        exit()

def fb_hack():
    logo()
    check_root()
    print(f"{C}[+] Connecting to Facebook Old Server...\n")
    time.sleep(2)
    print(f"{Y}[+] Scanning 2010-2012 Old IDs...\n")
    time.sleep(3)

    ids = ['100000723456789', '100000875432190', '100000543267890', '100001234567890', '100000678901234']
    passwords = ['123456', '112233', 'password', 'facebook123', 'qwerty']

    for i in range(5):
        uid = random.choice(ids)
        pw = random.choice(passwords)
        print(f"{G}[✓] ID: {uid} | Pass: {pw}")
        time.sleep(1.5)

    print(f"\n{Y}[!] Note: This is a prank tool for fun only.\n")
    input(f"{A}Press Enter to Exit...")

fb_hack()