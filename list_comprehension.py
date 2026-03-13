#Create a list of numbers 1,2,3,4,5
#Create another list of those numbers squared (calculate and use a loop)
#print the squared list
numbers = [1,2,3,4,5]
squares =[]

for number in numbers:
    squares.append(number ** 2)

print(squares)
#Using list comprehension
numbers = [1,2,3,4,5]
squares = [number ** 2 for number in numbers]

print(squares)

#Create a list of 3 names
#Use list comprehension to create another list of all those names in upper case
#print the new list
names = ["Michael","Mom","Person#1"]
upper_names = [name.upper() for name in names]
print(upper_names)

#Create a list of numbers from 1-10
#Populate another list with only the even numbers from the first list
#Print the new list

numbers = [1,2,3,4,5,6,7,8,9,10]
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print (even_numbers)

#Using list comprehension
numbers = [1,2,3,4,5,6,7,8,9,10]
even_numbers = [number for number in numbers if number % 2 == 0]
print (even_numbers)