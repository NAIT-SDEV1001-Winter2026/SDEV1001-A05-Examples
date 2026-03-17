def add(number1,number2):
    answer = number1 + number2
    return answer

def subtract(number1,number2):
    answer = number1 - number2
    return answer

def multiply(number1,number2):
    answer = number1 * number2
    return answer

def divide(number1,number2):
    answer = number1 / number2
    return answer

#__name__ is a dunder variable
#If this py file (calculator_tools.py) is run directly, __name__ contains "__main__"
#If this py file (calculator_tools.py) is NOT run directly(imported) it contains the name of the file that is being imported (calculator_tools)
print(__name__)
if __name__ == "__main__":
    #Demonstration Code
    print(add(6,3))
    print(subtract(6,3))
    print(multiply(6,3))
    print(divide(6,3))
