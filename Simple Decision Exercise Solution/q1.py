# Question 1: Prompt for two numbers and display if they are equal or not.
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

if number1 == number2:
    print("The numbers are equal.")
else:
    print("The numbers are NOT equal.")

#OR
result = " "
if number1 != number2:
    result = " NOT "

print (f"The numbers are{result}equal.")