# Declare the variables input from the user :

P = int(input("Enter the Principle Amount Please :"))
n = int(input("Enter the Number of Years :"))
r = float(input("Enter the rate of Interest :"))

# Declare the formula

A = P*(1+r/100)**n

# The Final Amount

print("The Total Amount including compound interest is :", A)