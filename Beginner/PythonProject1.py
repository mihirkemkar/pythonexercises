#You have been hired by the University of Data Science to manage their students' records. Your job is to create the student management system for the university. Let's try to build the system using basic Python operations.
#After completing this project, you will get to know how to solve basic Python problems. In this project, you will be applying the following concepts:
#Mathematical operations
#List operations
#Dictionary operations
#String indexing and formatting

class_1 = ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2 = ['Hilary Mason','Carla Gentry','Corinna Cortes']

new_class = class_1.extend(class_2)
print(new_class)

new_class.append('Peter Warden')
print("Updated Class :", new_class)

new_class.remove('Carla Gentry')
print("Updated Class :", new_class)

print("="*80)

Geoffrey_courses = {'Maths':65, 'English':70,'History':80,'French':70,'Science':60}
#print("The marks for Geoffrey Hinton are : ",Geoffrey_courses)

#total = sum(Geoffrey_courses)
#print("The total marks of Geoffrey Hinton from 500 is :", total)

#percentage = total/500*100
#print("The Percentage Geoffrey scored is : ", percentage)


mathematics = {'Geoffrey Hinton': 78,'Andrew Ng': 95,
'Sebastian Raschka':	65,
'Yoshua Benjio':	50,
'Hilary Mason':	70,
'Corinna Cortes':	66,
'Peter Warden':	75}

topper = max(mathematics, key=mathematics.get)
print(topper)