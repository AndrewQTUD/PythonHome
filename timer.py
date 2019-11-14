from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)



curr_datetime = datetime.now()
curr_hour = curr_datetime.hour()
print(curr_hour)