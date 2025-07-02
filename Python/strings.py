
"""
message = ' Hello, World '

print(message.strip())
print(message.upper())
print(message.split())
print(message.replace('r','s'))


#Operators with strings

str1 = 'Hello'
str2 = 'World'

print(str1 + " " + str2)


#Control statements

num = 0
if num > 0:
    print("This number is positive")
elif num == 0: 
    print("This number is zero")
else:
    print("This number is negative")
    


#Control statements

num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the second number: "))

if num1 > num1:
    print(num1, "is greater than", num2)
elif num2 > num1:
    print(num2, "is greater than", num1)
else:
    print("Both numbers are equal")
"""

"""
#LOOPS
#For loop
fruits = ['apple', 'banana', 'strawberry']
for fruit in fruits:
    print(fruit)

numbers = [1,2,3,5,7]
for number in numbers:
    print(number)


#While loop to count from 1 to 5

count = 1
while count <= 5:
    print(count)
    count +=1 #increment
   
    
    
   
    #Loop control statements
    #For loop
    
fruits = ['Apple','Banana','Cherry', 'Mango']
for fruit in fruits:
    if fruit == "Cherry":
        break   #Exits the loop if cherry is found
    print(fruit)
    
print()

for fruit in fruits:
    if fruit == "Cherry":
        continue    #Skips cherry and moves to the next
    print(fruit)
    
print()

for fruit in fruits:
    if fruit == "Cherry":
        pass    #placeholder, no action is needed for cherry
    print(fruit)
     """
 
 
 #Loop control statements
    #While loops
    
    
count = 0
while count < 5:
    print(count)
    count+=1
    if count == 3:
        break  #Exists the loop when the count is reached (3)
    
    
        