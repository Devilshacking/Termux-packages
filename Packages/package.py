#!/usr/bin/python3
import os
import time
import sys

# Clear screen
os.system("clear")

# Display banner
print('''\033[91m

  _______ ______ _____  __  __ _    ___   __  _____        _____ _  __          _____ ______ 
 |__   __|  ____|  __ \|  \/  | |  | \ \ / / |  __ \ /\   / ____| |/ /    /\   / ____|  ____|
    | |  | |__  | |__) | \  / | |  | |\ V /  | |__) /  \ | |    | ' /    /  \ | |  __| |__   
    | |  |  __| |  _  /| |\/| | |  | | > <   |  ___/ /\ \| |    |  <    / /\ \| | |_ |  __|  
    | |  | |____| | \ \| |  | | |__| |/ . \  | |  / ____ \ |____| . \  / ____ \ |__| | |____ 
    |_|  |______|_|  \_\_|  |_|\____//_/ \_\ |_| /_/    \_\_____|_|\_\/_/    \_\_____|______|
                                                                                                                                                                                      

CREATED BY Devil Hacking
''')

# Slow print function
def slowprint(s, delay=0.05):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)

# Display package options
print(''' \033[95m
+--------------------------------------+ 
| This Tool Installs All Basic Packages | 
+--------------------------------------+ 
|           Devil Hacking              |
+--------------------------------------+''')

slowprint(''' \033[93m
[01] python
[02] python2
[03] python-dev
[04] python3
[05] php
[06] java
[07] git
[08] perl
[09] bash
[10] nano
[11] curl
[12] openssl
[13] openssh
[14] wget
[15] clang
[16] nmap
[17] w3m
[18] hydra
[19] ruby
[20] macchanger
[21] host
[22] dnsutils
[23] coreutils
[24] fish
[25] zip
[27] tor
[28] hydra
[29] figlet 
[30] cowsay
[31] tar
[32] unzip
[33] vim
[34] ruby
[35] wcalc
[36] bmon
[37] unrar
[38] proot
[39] golang
[40] htop
[41] httping
[42] openssh
[43] ffmpeg
[44] Dnsutils
[45] Cowsay
[46] Screenfetch
[47] Sqlite
[48] Sshpass''')

slowprint('''\033[96m
This Command for access Storage in Termux
[00] termux-setup-storage''')

print ("                                            ")
choice = input("\033[93mDo You Want to Install All Packages [y/n] : ")
if choice == 'n':
    sys.exit()

if choice == 'y':
    os.system("apt update && apt upgrade -y")
    os.system("pkg install git -y")
    os.system("apt install python -y")
    os.system("apt install python2 -y")
    os.system("apt install python-dev -y")
    os.system("apt install python3 -y")
    os.system("apt install php -y")
    os.system("apt install java -y")
    os.system("apt install git -y")
    os.system("apt install perl -y")
    os.system("apt install bash -y")

    print("Please wait a moment...")

    os.system("apt install nano -y")
    os.system("apt install curl -y")
    os.system("apt install openssl -y")
    os.system("apt install openssh -y")
    os.system("apt install wget -y")
    os.system("apt install clang -y")
    os.system("apt install nmap -y")
    os.system("apt install w3m -y")
    os.system("apt install hydra -y")
    
    print("""Join our Telegram""")

    os.system("apt install ruby -y")
    os.system("apt install macchanger -y")
    os.system("apt install host -y")
    
    slowprint('''\033[95m|    t.me/Devils_hacking    |
    | Join Us On Telegram For Learn Ethical Hacking  |''')
    
    os.system("apt install dnsutils -y")
    os.system("apt install coreutils -y")
    os.system("apt install fish -y")
    os.system("apt install zip -y")
    os.system("apt install figlet -y")
    os.system("apt install cowsay -y")
    os.system("apt install unzip -y")
    os.system("apt install vim -y")
    os.system("apt install wcalc -y")
    os.system("apt install bmon -y")
    os.system("apt install unrar -y")
    os.system("apt install proot -y")
    os.system("apt install golang -y")
    os.system("apt install htop -y")
    os.system("apt install httping -y")
    os.system("apt install ffmpeg -y")
    os.system("apt install screenfetch -y")
    os.system("apt install sqlite -y")
    os.system("apt install sshpass -y")

    print("Allow the Button For Access the Storage in Termux")
    os.system("termux-setup-storage")

    # Final banner
    slowprint('''\033[95m|        Welcome To Devils Hacking          |
    |                   😈
    | Join Us On Telegram For Learn Ethical Hacking  |''')

    input("\n\nPress the enter key to exit : ")
