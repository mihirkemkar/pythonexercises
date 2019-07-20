num1, num2 = 5,0

try:
    quotient = num1/num2
    message = "Quotient is" + ' ' + str(quotient)
    where (quotient = num1/num2)

except ZeroDivisionError:
    message = "Cannot divide by zero"
    print(message)

