
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

R = '\033[31m'  # red
G = '\033[32m'  # green
C = '\033[36m'  # cyan
W = '\033[0m'  # white

def gmail():
	sender_address = input('\n'+ C + '[>] ' + G + 'Enter Your Gmail Email Address -> ' + W)
	sender_pass = input(C + '[>] ' + G + 'Enter Your Gmail Password-> '+W)
	receiver_address = input(C + '[>] ' + G + 'Enter Receiver Address -> ' +W)
	message = input(C + '[>] ' + G + 'Enter Medssage Body -> ')
	imp = input(C + '[>] '  + G + 'Do you want to Send mail as Important '  + R + '(y/n)'  +G + '-> '+W)
	mail_content = '''
	{}
	'''.format(message)
	message = MIMEMultipart()
	message['From'] = sender_address
	message['To'] = receiver_address
	message['X-Priority'] = '{}'.format(imp)
	message['Subject'] = input(C + '[>] ' + G + 'Enter Subject -> ')
	message.attach(MIMEText(mail_content, 'plain'))
	try:
		session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
		session.starttls() #enable security
		session.login(sender_address, sender_pass) #login with mail_id and password
		text = message.as_string()
		session.sendmail(sender_address, receiver_address, text)
		session.quit()
		print(C + '[+] ' +G + 'Mail Successfully Send....')
	except smtplib.SMTPAuthenticationError as e:
		print(R + '[!] Check the Password and Try Again' +W)
		email()


