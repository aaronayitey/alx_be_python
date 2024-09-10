# Import the date from the datetime library
from datetime import date

# This script calculates the future age from a user with user inputs by 2050

# Accept input
current_age = int(input("How old are you? "))

# Get current year
current_year = int(date.today().strftime("%Y"))

# Get the difference from 2050
year_difference_by_2050 = 2050 - current_year

# calculate age by 2050
age_by_2050 = current_age + year_difference_by_2050

print(f"In 2050, you will be {age_by_2050} years old.")