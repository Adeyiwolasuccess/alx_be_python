# Prompt the user for their monthly income
monthly_income_str = input("Enter your monthly income: ")
monthly_income = float(monthly_income_str)  # Convert to float for financial calculations

# Prompt the user for their total monthly expenses
monthly_expenses_str = input("Enter your total monthly expenses: ")
monthly_expenses = float(monthly_expenses_str)  # Convert to float

# Calculate Monthly Savings
monthly_savings = monthly_income - monthly_expenses

# Define the annual interest rate
annual_interest_rate = 0.05  # 5%

# Calculate the total savings over a year without interest
total_savings_before_interest = monthly_savings * 12

# Calculate the interest earned over the year on the total principal saved
# Using the simplified approach: interest on the sum of monthly savings accumulated over the year
# The problem states: Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05)
# This implies the interest is calculated on the total amount saved over the year.
interest_earned = total_savings_before_interest * annual_interest_rate

# Calculate the projected annual savings including interest
projected_annual_savings = total_savings_before_interest + interest_earned

# Output Results
# Display the user’s monthly savings
print(f"Your monthly savings are ${monthly_savings:.2f}.") # Using .2f to format as currency

# Display the projected annual savings after including interest
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings:.2f}.") # Using .2f