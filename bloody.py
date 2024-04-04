from datetime import datetime, timedelta

def days_until_next_donation(last_donation_date_str):
    # Parse the input date string
    last_donation_date = datetime.strptime(last_donation_date_str, "%d/%m/%Y")
    
    # Calculate the next eligible donation date
    next_donation_date = last_donation_date + timedelta(days=90)
    
    # Calculate the number of days until the next donation
    days_until_donation = (next_donation_date - datetime.now()).days
    
    return days_until_donation

def main():
    last_donation_date_str = input("Enter the date of your last donation (dd/mm/yyyy): ")
    
    try:
        days_until_donation = days_until_next_donation(last_donation_date_str)
        if days_until_donation <= 0:
            print("You are eligible to donate blood now!")
        else:
            print(f"You need to wait {days_until_donation} days until you can donate blood again.")
    except ValueError:
        print("Invalid date format. Please use the format dd/mm/yyyy.")

if __name__ == "__main__":
    main()
