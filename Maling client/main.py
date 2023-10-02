#use to sent mail
import smtplib

#use to create the email
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

#spesifying the smtp server need to add the smtp server address and the port number
server = smtplib.SMTP('smtp.gmail.com',587)

#starting the server
server.ehlo()

#adding the email and the password to send the email
server.login('email@gmail.com','password123')

#creating the email
msg = MIMEMultipart()
msg['From'] = 'abc@gmail.com'
msg['To'] = 'bcd@gmail.com'
msg['subject'] = 'Just testing email'

#open the message file
with open('message.txt', 'r') as msg_con:
    message = msg_con.read()

msg.attach(MIMEText(message,'plain text'))

#image name
attach_filename = 'download.jpeg'
attachment = open(attach_filename,'rb')

p = MIMEBase('application','octet-stream')
#read the content
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('content-Disposition', f'attachment; filename={attach_filename}')
msg.attach(p)

text = msg.as_string()
#sender and the target
server.sendmail('abc@gmail.com','test@gmail.com',text)
