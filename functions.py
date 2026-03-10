#A bunch of code that is given a name
#Called by name
#can return a value
#Values passed to functions whent they are called are called arguments and the arguments are accepted into parameters
#Parameter values are not optional
#Should perform a singular task

#ask for a name and display a welcome
# name = input("Enter your name: ")
# print (f"Welcome {name}!")

#Using functions(must be coded before the code that uses the function)
def get_name():
    name = input("Enter your name: ")
    return name #return returns a value to where the functions was called from

def display_name(name):
    print (f"Welcome {name}!")

# name = get_name()#call the get_name() and assign what it returns to name variable
# display_name(name)

#multiple parameters
def add_numbers(number1,number2):
    answer = number1 + number2
    return answer

test = add_numbers(5,3)
print (test)
#or
print(add_numbers(5,3))

#default parameter values
def display_favorite_color(color = "Green"):
    print(f"Your favorite color is {color}")

display_favorite_color("Blue")
display_favorite_color()
    