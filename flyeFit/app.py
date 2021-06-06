import datetime
import requests
from bs4 import BeautifulSoup
import time
"""
    The following script books specified sessions for
    tomorrow in flyefiet gym web app.
"""

# Very sensitive data
credentials = {
    'email_address': '',
    'password': ''
}

str_tomorrow = (datetime.date.today() +
                datetime.timedelta(days=1)).strftime("%Y-%m-%d")

url_booking = "https://myflye.flyefit.ie/myflye/book-workout/167/5/{}".format(
    str_tomorrow)  # Change the last digit in the URL to change to which GYM you want to book .i.e. Liffey Valley = 15, Georges = 5

# Set each slot to True to book
slots = {
    "05:30 - 07:00": False,
    "07:00 - 08:30": False,
    "08:30 - 10:00": False,
    "10:00 - 11:30": False,
    "11:30 - 13:00": False,
    "13:00 - 14:30": False,
    "14:30 - 16:00": False,
    "16:00 - 17:30": False,
    "17:30 - 19:00": False,
    "19:00 - 20:30": True,  # Book this one
    "20:30 - 22:00": False
}

slots1 = {
    "07:30 - 09:00": False,
    "09:00 - 10:30": False,
    "10:30 - 12:00": False,
    "12:00 - 13:30": True,
    "13:30 - 15:00": False,
    "15:00 - 16:30": False,
    "16:30 - 18:00": False,
    "18:00 - 19:30": False
}

# Login
session = requests.Session()
session.post("https://myflye.flyefit.ie/login", data=credentials)
print("[DEBUG] Logging in {} ...".format(credentials['email_address']))
# Get the sessions tomorrow
soup = BeautifulSoup(session.get(url_booking).text, 'html.parser')

for slot in slots1:
    if slots1[slot] == True:
        print("[DEBUG] Slot: {} | Checking... ".format(slot))
        course_field = soup.find(
            text=slot).parent.parent.parent.select("p.btn-primary")[0]
        if course_field.text.strip() == 'Not Yet Open':
            print("[ERROR] Slot: {} is Not Open Yet. ".format(slot))
        elif course_field.text.strip() == 'Booked':
            print("[DEBUG] Slot: {} is Already Booked. ".format(slot))
        elif hasattr(course_field, 'data-course-id'):
            session.post("https://myflye.flyefit.ie/api/course_book",
                         data={'course_id': course_field['data-course-id']})
            print("[DEBUG] Slot: {} is Now Successfuly Booked. ".format(slot))
        else:
            print("[ERROR] Slot: {} | Parsing error.".format(slot))
