#!/usr/bin/env python3
import subprocess as subp
import requests
from modules.website import web
from modules.e import gmail

R = '\033[31m'  # red
G = '\033[32m'  # green
C = '\033[36m'  # cyan
W = '\033[0m'  # white

VERSION = '1.0'

def banner():
	banner = r'''

   _      __    __    ___ _     _     _     
  /_\    / /   / /   / _ \ |__ (_)___| |__  
 //_\\  / /   / /   / /_)/ '_ \| / __| '_ \ 
/  _  \/ /___/ /___/ ___/| | | | \__ \ | | |
\_/ \_/\____/\____/\/    |_| |_|_|___/_| |_|
											
'''
	print(G + banner + W)
	print(R + 'A Complete Phishing Tool'+W +'\n')
	print(R + "Created By :- " + G + "Hacker Destination" + W)
	print(R + "Version :- " + G + VERSION + W + '\n')


def menu():
	choice ='0'
	while choice =='0':
		print("")
		print(C + '[>] ' + G + 'Attack Mode' +W +'\n')
		print(R + '[1] ' + G +  'Gamil Phishing'  + W)	
		print(R + '[2] ' + G +  'Webiste Phishing'  + W + '\n')
		choice = input(G + '[+]' + C + " Enter Option No. ->  " + W )
		if choice == "1":
			gmail()
		elif choice == "2":
			web()
		else:
			print('\n' + R + "[!] I don't understand your choice" +W)
			return menu()

try:
	banner()
	menu()
except KeyboardInterrupt:
	print('\n' + R + '[!]' + R + ' Keyboard Interrupt.' + W)
	exit()
