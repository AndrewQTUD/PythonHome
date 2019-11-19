import requests
from bs4 import BeautifulSoup
import smtplib
from datetime import datetime, timedelta
from time import time, ctime




cd = datetime.now()
listOfEmails = ["andytown@live.ie", "andysempai12@gmail.com", "zalaru.raluca@gmail.com"]



print('Enter your subject line.')
subject = input()



print('Enter the body of your message.')
body = input()

body = body + ' ' + str(cd)





    
def transferInfo(body, subject):
    def send_mail():
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
    
        server.login('andysempai12@gmail.com', 'ocbhdmemnkvkvzea')

        

        
        
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
transferInfo(body,subject) 

    