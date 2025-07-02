"""
fruits = ['Apple','Banana','Cheery']
print(fruits[0])
fruits[1] = 'Blueberry'
print(fruits)
"""

#Adding and removing items from a list

fruits = ['Apple','Banana','Strawberry']
fruits.append('Kiwi') # Add at the end
print(fruits)

fruits.insert(1,'Orange') #insert at a specific position
print(fruits)

fruits.sort(reverse=True)
print(fruits)
