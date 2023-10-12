#for environment variable in order to conceal password.
'to make use of environment variable, create a .env file in your root folder, then input the variable name and your password
i.e MY_PWD = abc123*'
import os
from dotenv import load_dotenv

#for email
import smtplib
from email.message import EmailMessage
from email.utils import COMMASPACE, formatdate

#Set up your email configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587
'replace abc@gmail.com and xyz@anymail.com into appropriate mail'
sender_mail_address = 'abc@gmail.com'
receiver_mail_address = ['xyz@anymail.com']

#import password
load_dotenv()
"replace 'ENV_VAR' with the name of environment variable you stored your password with"
password = os.environ['ENV_VAR']
email_subject = 'Title of the Email'
email_body = '''This contains the email body
allows
multiline.'''

#if it includes file
file_name = 'file name'
file_path = '/file path'

def send_mail(send_mail_from, send_mail_to, mail_subject, mail_body, file_path, file_name):
    assert isinstance (send_to, list)
    msg = EmailMessage()
    msg['From'] = send_mail_from
    msg['To'] = COMMASPACE.join(send_mail_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] mail_subject
    msg.set_content(mail_body)

    if (file_name != '' && file_path != ''):
        with open(file_path, 'rb') as attachment:
            msg.add_attachment(attachment.read(), maintype='application', subtype='octet-stream', filename=file_name)

    try:
        with smtplib.SMTP(smtp_server, smtp_port)
as server:
            server.starttls()
            server.login(sender_address, password)
            server.send_message(msg)
        print("Email sent successfully!")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
