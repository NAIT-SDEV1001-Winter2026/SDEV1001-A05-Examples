number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))

#AND
#All conditions must be TRUE for the entire condition to be true
if number1 == 5 and number2 == 8:
    print("Number 1 is 5 and number 2 is 8")

#OR
#IF any of the conditions are TRUE, the entire condition is True
if number1 == 5  or number2 == 8:
    print("At least one condition is True")

#And has precedence over or
#Brackets have precedence over everything

#if x == 5 and y == 2 or z > 1 and name =="Homer" or age == 99
