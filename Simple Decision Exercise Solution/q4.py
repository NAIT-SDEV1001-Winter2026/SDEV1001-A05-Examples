# Question 4: Prompt for three numbers and display the highest value.

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
third = int(input("Enter third number: "))

highest = first

if second > highest:
    highest = second
if third > highest:
    highest = third

print (f"The highest value is {highest}")