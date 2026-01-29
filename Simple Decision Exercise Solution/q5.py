# Question 5: Prompt for a number and display if it is even or odd.

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is EVEN")
else:
    print("The number is ODD")

result = "ODD"
if number % 2 == 0:
    result = "EVEN"

print (f"The number is {result}")

