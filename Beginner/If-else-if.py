#In this task you are going to make use of the if-elif-else statement to find out if a number is positive, negative or zero.
#A variable num = 5 is given along with another variable condition=None (captures the state of num)
#Put the conditions for checking whether the number is positive (+) , negative (-) or zero (0) using if-elif-else construct.
#If num is greater than 0 set condition=positive. Print out the variable condition.
#Else num is less than 0, set condition=negative. Print out the variable condition.
#Else num is equal to 0 set condition=zero. Print out the variable condition.

num = 5
condition = None



if num < 0:
    condition = "negative"
    #print("The number is negative")
    #condition = negative
elif num == 0:
    #print("The number is zero")
    condition = "zero"
if num > 0:
    condition = "positive"
    #print("The number is positive")

print(condition)

