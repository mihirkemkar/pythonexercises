# Initialize Variables
name, title = 'Monty' , 'Python'

# Concatenate to Variables name and title and save it to variable called full_name.

full_name = name + ' ' + title
print(full_name)

first_name = name[0:5]
print(first_name)

print(len(full_name))

print(full_name)
len_name = full_name.replace(" ", "")
print(len_name)
print(len(len_name))


is_f = 'f' in full_name
print(is_f)

split = full_name.split(" ")
stringcount = len(split)
print(split)

print("\n\n")
print(full_name)
print(first_name)
print(len_name)
print(is_f)
print(split)