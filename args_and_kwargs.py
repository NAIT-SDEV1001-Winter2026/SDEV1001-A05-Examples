#function to accept and add 2 numbers together and return the sum
def add_2_numbers(number1, number2):
    sum  = number1 + number2
    return sum

print(add_2_numbers(5,3))
#Good! but can only add 2 numbers :(
#What if we wanted to do this?
# print(add_numbers(5,7,3,88,4,6,6,77,44,3))
# #or
# print(add_numbers(5,7,3,88,4,6,6))

#use *args to perfrom this task
#An *arg parameter allows a variable number of arguments to be passed to it.The values are store in a tuple
#The * in the param name means it is an arg parameter, but the name can be anything

#function to add any number of numbers and return the sum
def add_any_numbers(*numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum

print(add_any_numbers(4,7,5,99,55,44,777,23232,55,33,754,1,4343,656,23,2,233,2222))

# * placed in front of a param means to take the values and "pack" them into a tuple of the same name
# * placed in front of a collection (list/tuple) is called an unpacking operator and returns all the values in the collection

grades = [66,73,77,99,33]
print(grades)

#Unpack the list
print(*grades)

print("Shane")
print(*"Shane")

#Use **Kwargs are used for key-value pairs of data
#Kwargs keys/values are stored in a dictionary

#Create function that will:
    #Have a parameter called sport and will display that sport
    #Have a parameter for a number of scores and display them

def sport_stuff(sport,*scores,**staff):
    print(f"The sport is: {sport}")
    
    print("Scores:")
    for score in scores:
        print(score)

    print("Staff:")
    for position,name in staff.items():#items() returns the key and the value
        print(f"{position}: {name}")


sport_stuff("Soccer",3,6,3,2,4,coach = "Yoda", assistant_coach = "Darth Vader", water_boy = "Jar Jar Binks")


