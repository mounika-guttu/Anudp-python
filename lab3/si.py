

# Get user input
principal = float(input("Enter the principal amount (P): "))
rate = float(input("Enter the annual interest rate (R in %): "))
time = float(input("Enter the time (T in years): "))

# Calculating Simple Interest
simple_interest = (principal * rate * time) / 100

#the result
print(f"\nSimple Interest = ₹{simple_interest:.2f}")
