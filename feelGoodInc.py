import requests
from bs4 import BeautifulSoup
import smtplib
from datetime import datetime, timedelta
from time import time, ctime

cd = datetime.now()


    

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('andysempai12@gmail.com', 'ocbhdmemnkvkvzea')

    subject = 'You can do it Raluca!'

    body = 'This is an automated email to remind you that you can do anything!'

    msg = f"Subject : {subject}\n\n{body}"

    server.sendmail(
        #Test e-mail
        'andysempai12@gmail.com',
        #Another test e-mail
        'andytown@live.ie',
        #Destination e-mail
        msg
    )
    print("e-mail sent " + str(cd))

    server.quit()

send_mail()    
    