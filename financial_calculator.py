import math

# Introduction to the calculator helps the user navigate and prompts the user to choose between 'investment' or 'bond'.
print("Welcome to your financial calculator. Are you interested in investment, ROI or a home loan?")
print("Please enter either 'investment', 'roi', 'savings' or 'bond' from the menu above to proceed:")

# Corrected the assignment to use '=' instead of '=='
user_entry = input(" ")

# Validate user input and perform calculations.
if user_entry.lower() == 'investment':
    # Investment calculation
    principal = float(input("Enter the amount of money you are depositing: "))
    interest_rate = float(input("Enter the interest rate (as a percentage): "))
    years = int(input("Enter the number of years you plan on investing: "))
    interest_type = input("Do you want 'simple' or 'compound' interest? ")

    # If the user chooses simple interest calculation for their investment:
    if interest_type.lower() == 'simple':
        interest = (principal * (interest_rate / 100) * years)

    # If user chooses compound interest calculation for their investment:
    elif interest_type.lower() == 'compound':
        interest = principal * math.pow((1 + (interest_rate / 100)), years) - principal
    else:
        print("Invalid interest type entered. (Please enter ONLY the number of interest NOT the percentage sign.)")
        interest = 0

    # Display the result of the calculation.
    print(f"Your {interest_type} interest will be: {interest:.2f}")

    # Return on Investment (ROI) calculation.
elif user_entry == 'roi':
    initial_investment = float(input("Enter the initial investment amount: "))
    final_value = float(input("Enter the final value of the investment: "))

    # ROI calculation.
    roi = ((final_value - initial_investment) / initial_investment) * 100

    # Display the result of the calculation.
    print(f"Your Return on Investment (ROI) is: {roi:.2f}%")

    # Savings Goal Calculator.
elif user_entry == 'savings':
    savings_goal = float(input("Enter your savings goal here: "))
    interest_rate = float(input("Enter the annual interest rate (as a percentage): "))
    years = int(input("Enter the number of years to reach your savings goal: "))

    # Monthly savings calculation.
    i = (interest_rate / 100) / 12
    monthly_savings = savings_goal / ((math.pow((1 + i), years * 12) - 1) / i)

    # Display the result of the calculation.
    print(f"To reach your savings goal in {years} years, you need to save approximately: {monthly_savings:.2f} per month.")

# Bond calculation.
elif user_entry.lower() == 'bond':
    current_value = float(input("Enter the current value of the property: "))
    interest_rate = float(input("Enter the interest rate: "))
    months = int(input("Enter the total number of months you plan to repay your loan: "))

    # Monthly interest calculation.
    i = (interest_rate / 100) / 12

    # Bond repayment calculation.
    repayment = (i * current_value) / (1 - math.pow((1 + i), - months))

    # Display the result of the calculation:
    print(f"Your monthly loan installment will be: {repayment:.2f}")

else:
    print("Invalid entry. Please enter either 'investment' or 'bond'.")

