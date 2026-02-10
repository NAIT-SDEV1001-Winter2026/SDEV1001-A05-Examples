#Strings are a list of characters
#loop through a string and print each letter on its own line
# string = "Have a groovy Tuesday!"
# for letter in string:
#     print(letter)

#Ask the user for a string and print how many vowels are in the string
#Enter a string: Happy Tuesday!
#There are 4 vowels in 'Happy Tuesday'

# string  = input("Enter a string: ")

# vowels = "aeiou"
# count = 0

# for letter in string:
#     if letter in vowels:
#         count += 1
# print (f"There are {count} vowels in {string}")

#RANGE LOOPS
#range() generates a sequence of numbers that can be used for a loop counter

#Syntax
#range(start,stop,step)
#start is inclusive, the stop value is exclusive
1,2,3,4,5
#print numbers from 1 to 5
for number in range(1,6):
    print (f"Number: {number}")

#calculate and print the cubes of numbers from 0 to 4
#0 cubed is 0
#1 cubed is 1

for number in range(0,5):
    print (f"{number} cubed is {number ** 3}")

#if the range starts at 0 you can omit the start value
for number in range(5):
    print (f"{number} cubed is {number ** 3}")

#print the even numbers between 4 and 20
for number in range (4,21,2):
    print(number)

#ask the user how many Hello world to print
how_many = int(input("how many 'Hello World' to print? "))
for count in range (how_many):
    print ("Hello World")

#print a string a certain number of times
print ("Hello " * 5)

#Ask the user for how many rows to print of a right angle triangle
#How many rows in the triangle: 5
#*
#**
#***
#****
#*****
how_many = int(input("How many rows to print: "))
for count in range(1,how_many + 1):
    print("*" * count)

#upside down
how_many = int(input("How many rows to print: "))
for count in range (how_many,0,-1):
    print("*" * count)


how_many = int(input("How many rows to print: "))
for count in range(1,how_many + 1):
    print(" " * 10 + "*" * count)

