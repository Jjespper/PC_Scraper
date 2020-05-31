import smtplib
from configparser import ConfigParser

config = ConfigParser()
config.read('/home/jacobo/Config_Trash/config.ini')
gmail_user = config['EMAIL']['user']
gmail_password = config['EMAIL']['password']


sent_from = gmail_user
to = [input()]
subjet = 'Prueba'
email_text = "Prueba de smtplib"


#email send request
try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print ('Email sent!')
except Exception as e:
    print(e)