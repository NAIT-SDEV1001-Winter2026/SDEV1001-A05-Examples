#Python debugger
#n - next line
#l - list surrounding lines of code
#ll - list more surrounding lines of code
#c - continues to the end of the program OR the next break point
number1 = 5
number2 = 8
# breakpoint()
answer = number1 + number2

print (f"The sum of {number1} and {number2} is {answer}")
# breakpoint()
if answer > 10:
    print("Over 10")
else:
    print("not over 10")