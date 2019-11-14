import requests
from bs4 import BeautifulSoup
import smtplib
from datetime import datetime, timedelta
from time import time, ctime

cd = datetime.now()
listOfEmails = ["andytown@live.ie", "andysempai12@gmail.com", "zalaru.raluca@gmail.com"]



    

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('andysempai12@gmail.com', 'ocbhdmemnkvkvzea')

    subject = 'You can do it Raluca!'

    body = 'This is an automated email to remind you that you can do anything! ' + str(cd) + ' There are : ' 
    + str(len(listOfEmails)) + ' other in the e-mail list'

    msg = f"Subject : {subject}\n\n{body}"

    server.sendmail(
        #Sender
        'andysempai12@gmail.com',
        #recipent
        'andytown@live.ie',
        
        msg
    )

    server.sendmail(
        #Sender
        'andysempai12@gmail.com',
        #recipent
        'zalaru.raluca@gmail.com',
        
        msg
    )
    print("e-mail sent " + str(cd))

    server.quit()

send_mail()    
    