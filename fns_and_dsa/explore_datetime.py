# Import the datetime library
from datetime import datetime, timedelta

def display_current_datetime():
    """Display the current date and time"""

    current_date = datetime.now()
    
    print(f"Current date and time: {current_date.strftime("%Y-%m-%d %H:%M:%S")}")



def calculate_future_date():
    """Calculate the future date by adding a number of days to the current date"""
    try:
        number_of_days = int(input("Enter number of days: "))

    except ValueError:
        print("Enter numbers only!")
    return
    
    future_date = datetime.now() + timedelta(days=number_of_days)

    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")


if __name__ == '__main__':
    display_current_datetime()

    calculate_future_date()