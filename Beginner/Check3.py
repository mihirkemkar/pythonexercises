
num1 , num2 = 5,0

try:
    quotient = num1 / num2
    message = "Quotient is" + ' ' + str(quotient)
    print(message)
except ZeroDivisionError:
   message = "Cannot divide zero"
   print(message)