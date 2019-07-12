fruits = {'apple':"green", 'banana':"yellow", 'cherry':"red"}
print(fruits)

#Change the color of the apple from green to red

u1 = {'apple':'red'}
fruits.update(u1)
print(fruits)

# Add another fruit as guava
g1 = {'guava': 'green'}
fruits.update(g1)
print(fruits)

# Delete cherry from the list
del fruits['cherry']
print(fruits)