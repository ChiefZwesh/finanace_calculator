import math 

# Define header and sub-headers
def print_header(text):
    print("=" * 60)
    print(text.center(60))
    print("=" * 60)

def print_subheader(text):
    print("-" * 60)
    print(text.center(60))
    print("-" * 60)

# Print main header
print_header("Finance Calculator")

# Print investment and bond options
print("Investment - to calculate the amount of interest you'll earn on your investment")
print("Bond - to calculate the amount you'll have to pay on a home loan")
print()

# Print sub-header for user input
print_subheader("Category:")
print()

# Prompt user for input
user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()
print()

# Print sub-header for product specifications
print_subheader("Product Specifications:")
print()

# Calculate investment or bond based on user choice
if user_choice == "investment":
    deposit = float(input("Please enter the amount you are depositing: "))
    interest_rate = float(input("Please enter the interest rate. (Please enter the integer excluding %): ")) / 100
    duration = float(input("Please enter the duration of the investment in years: "))
    interest = input("Please enter simple or compound to proceed: ").lower()
    
    if interest == "simple":
        investment_simple_interest_calc = deposit * (1 + (interest_rate * duration))
        print()
        print(f"The sum total of your investment amount will be: R {investment_simple_interest_calc:.2f}")
    elif interest == "compound":
        investment_compound_interest_calc = deposit * (1 + interest_rate) ** duration
        print()
        print(f"The sum total of your investment amount will be: R {investment_compound_interest_calc:.2f}")
    else:
        print()
        print("Invalid input. Please try again")

elif user_choice == "bond":
    deposit = float(input("Please enter the present value of the house: "))
    interest_rate = float(input("Please enter the interest rate. (Please enter the integer excluding %): ")) / 100 / 12
    bond_duration = float(input("Please enter the duration of the bond in months: "))
    print()
    bond_calc = (interest_rate * deposit) / (1 - (1 + interest_rate) ** (-bond_duration))
    print(f"The amount you will have to pay on your bond is: R {bond_calc:.2f}")
else:
    
    print()
    print("Invalid input. Please try again")
