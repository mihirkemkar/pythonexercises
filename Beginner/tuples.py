# Creating a new tuple.

weights_new = (70,80,48,50)
print("The newly created tuple is : ", weights_new)

# Calculate the maximum and minimum weights using the max() and min() functions respectively on the new weights_new tuple. Save them to the maximum and minimum variables.

maximum = max(weights_new)
minimum = min(weights_new)

print("The weight_new tuple with the maximum value : ", maximum)
print("The weight_new tuple with the minimum value : ", minimum)

#Now calculate the sum of the weights using the sum() function and save it to sum_weights.

sum_weights = sum(weights_new)
print("The sum of the following weights_new tuple is ", sum_weights)

#Save the mean of their weights (using the formula sum / number of elements) to a mean_new variable.

mean_new = sum_weights/4
print("The mean of the following weights_new tuple is ", mean_new)