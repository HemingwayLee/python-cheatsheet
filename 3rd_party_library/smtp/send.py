import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os.path import join, dirname
from dotenv import load_dotenv

DOTENV_PATH = join(dirname(__file__), '.env')
load_dotenv(DOTENV_PATH)
PASSWORD = os.environ.get("PASSWORD")
MYMAIL = os.environ.get("MYMAIL")

mail_content = '''
Hello,
This is a simple mail. There is only text, no attachments are there The mail is sent using Python SMTP library.
Thank You
'''

#The mail addresses and password
sender_address = MYMAIL
sender_pass = PASSWORD
receiver_address = MYMAIL

#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'A test mail sent by Python. It has an attachment.'
message.attach(MIMEText(mail_content, 'plain'))
session = smtplib.SMTP('smtp.gmail.com', 587) 
session.starttls() 
session.login(sender_address, sender_pass) 
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')


