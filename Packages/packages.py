#!/usr/bin/python3
import os
import time
import sys

# Clear screen
os.system("clear")

# Display banner
print(r''' \033[91m
  _______ ______ _____  __  __ _    ___   __  _____        _____ _  __          _____ ______ 
 |__   __|  ____|  __ \|  \/  | |  | \ \ / / |  __ \ /\   / ____| |/ /    /\   / ____|  ____|
    | |  | |__  | |__) | \  / | |  | |\ V /  | |__) /  \ | |    | ' /    /  \ | |  __| |__   
    | |  |  __| |  _  /| |\/| | |  | | > <   |  ___/ /\ \| |    |  <    / /\ \| | |_ |  __|  
    | |  | |____| | \ \| |  | | |__| |/ . \  | |  / ____ \ |____| . \  / ____ \ |__| | |____ 
    |_|  |______|_|  \_\_|  |_|\____//_/ \_\ |_| /_/    \_\_____|_|\_\/_/    \_\_____|______|
                                                                
CREATED BY Devils Hacking
\033[0m''')

# Slow print function
def slowprint(s, delay=0.05):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)

# Display package options
print(r''' \033[95m
+--------------------------------------+ 
| This Tool Installs All Basic Packages | 
+--------------------------------------+ 
|           Devils Hacking              |
+--------------------------------------
\033[0m''')

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
[28] figlet 
[29] cowsay
[30] tar
[31] unzip
[32] vim
[33] wcalc
[34] bmon
[35] unrar
[36] proot
[37] golang
[38] htop
[39] httping
[40] ffmpeg
[41] sqlite
[42] sshpass
\033[0m''')

slowprint('''\033[96m
This Command for access Storage in Termux:
[00] termux-setup-storage
\033[0m''')

# Get user choice
choice = input("\033[93mDo You Want to Install All Packages [y/n] : \033[0m")
if choice.lower() == 'n':
    sys.exit()

if choice.lower() == 'y':
    os.system("apt update && apt upgrade -y")
    
    # List of packages to install
    packages = [
        "python", "python2", "python3", "php", "java", "git", "perl", "bash", 
        "nano", "curl", "openssl", "openssh", "wget", "clang", "nmap", "w3m", 
        "hydra", "ruby", "macchanger", "host", "dnsutils", "coreutils", "fish", 
        "zip", "figlet", "cowsay", "tar", "unzip", "vim", "wcalc", "bmon", 
        "unrar", "proot", "golang", "htop", "httping", "ffmpeg", "sqlite", "sshpass"
    ]
    
    for pkg in packages:
        os.system(f"apt install {pkg} -y")
    
    os.system("termux-setup-storage")
    
    # Final message
    slowprint('''\033[95m
+----------------------------------------+
|     Welcome To Devils Hacking          |
|        Join us @Devils_hacking         |
| Learn Ethical Hacking on Telegram!     |
+----------------------------------------+
\033[0m''')

    input("\n\nPress the enter key to exit: ")
  
