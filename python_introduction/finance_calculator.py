# A script that asks user for her/his monthly /
# income and expenses and calculates his savings with interest after a year.
monthly_income = float(input("Enter your monthly income: ")) 
monthly_expenses = float(input("Enter your total monthly expenses: "))

savings = monthly_income - monthly_expenses

projected_savings = ((savings * 12) + (savings * 12 * 0.05))

print(f"Your monthly savings are ${savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")
