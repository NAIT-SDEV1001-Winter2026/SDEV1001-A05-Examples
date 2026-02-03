# 2.	create a file named leap_year.py in this folder. Write a program to determine if a user input year is a leap year. A year is a leap year if it is divisible by 4 but not by 100, or if it is divisible by 400. 

#Get year from user
user_input = int(input("Enter a year: "))

#Determine if it is a leap year and print message
if (user_input % 4 == 0 and user_input % 100 != 0) or (user_input % 400 == 0):
    print(f"Is {user_input} a leap year? True")
else:
    print(f"Is {user_input} a leap year? False")

#OR
if (user_input % 4 == 0 and user_input % 100 != 0) or (user_input % 400 == 0):
    result = "True"
else:
    result = "False"

print(f"Is {user_input} a leap year? {result}")
