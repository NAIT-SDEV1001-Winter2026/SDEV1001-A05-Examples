# Question 2: Prompt for two numbers and display the highest value or if they are equal.

#prompt for 2 numbers
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

#print the highest or equal message
if number1 > number2:
    print(f"The highest value is {number1}.")
elif number1 < number2:
     print(f"The highest value is {number2}.")
else:
     print(f"{number1} and {number2} are equal")