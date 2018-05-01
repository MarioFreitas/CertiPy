import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from configs import *

def send_mail(email_user, email_password, email_send, subject, body, filename):
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject

    msg.attach(MIMEText(body,'plain'))

    attachment = open(filename,'rb')

    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition','attachment', filename=filename.split('\\')[-1])

    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_user,email_password)

    server.sendmail(email_user,email_send,text)
    server.quit()

email_user = os.environ.get('CIVCOM_EMAIL')
email_password = os.environ.get('CIVCOM_PASSWORD')
subject = f'Certificado CivCom - {curso}'

with open(alunosFile, 'r') as f:
    for line in f:
        l = line.strip()
        l = line.split(', ')
        aluno = l[0]
        email_send = l[1]

        body = f'Caro(a) {aluno},\n\nSegue em anexo o seu certificado do {curso}.'

        fname = f'{aluno} {curso}'
        fname = ''.join(fname.split(' '))

        filename = f'certificados\\PDFs\\{fname}.pdf'

        send_mail(email_user, email_password, email_send, subject, body, filename)