# Question 3: Prompt for two numbers and display the highest value
# and whether it was the first or second number entered.
first = int(input("Enter number 1: "))
second = int(input("Enter number 2: "))

if first > second:
    print(f"The highest number between {first} and {second} is {first} and it was the first number entered!")
elif second > first:
    print(f"The highest number between {first} and {second} is {second} and it was the second number entered!") 
else:
    print("Both numbers are equal")