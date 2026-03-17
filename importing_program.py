#When we import using import * we import everything from that module. To not execute the mainline code from the imported module we use a main guard(coded on the imported file)

from calculator_tools import *

#from calculator_tools import add


number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))

sum = add(number1,number2)

print (f"The sum is: {sum}")

