#Handle unexpected/expected situations that could cause crashes gracefully with nice error messages and keep the program thing
#try/except
#try - if an excpetion occurs in the try block  it will jump to the except block
#except - addresses the exception and at minimum displays a nice error message

# try:#Try this code
#     numerator = int(input("Enter the numerator: "))
#     denominator = int(input("Enter the denominator: "))
#     quotient = numerator/denominator

#     print (f"The quotient is {quotient}")

# except:#end up here if an exception occurs in the try
#     print("Something went BOOM!")

# print("Have a groovy day!")

#The above code is good BUT the error message is not specific
# try:#Try this code
#     numerator = int(input("Enter the numerator: "))
#     denominator = int(input("Enter the denominator: "))
#     quotient = numerator/denominator

#     print (f"The quotient is {quotient}")
# except ValueError:
#     print ("You must enter an integer")
# except ZeroDivisionError:
#     print ("The denominator cannot be 0!")

# except:#end up here if an exception occurs in the try
#     print("Something went BOOM!")

# print("Have a groovy day!")

#sometimes we want a nice message and the python message
# try:#Try this code
#     numerator = int(input("Enter the numerator: "))
#     denominator = int(input("Enter the denominator: "))
#     quotient = numerator/denominator

#     print (f"The quotient is {quotient}")
# except ValueError as error_message:
#     print (f"You must enter an integer! ({error_message})")
# except ZeroDivisionError as error_message:
#     print (f"The denominator cannot be 0! ({error_message})")

# except Exception as error_message:#end up here if an exception occurs in the try
#     print(f"Something went BOOM! ({error_message})")

# print("Have a groovy day!")

#Best practices
    #Keep try blocks small
    #Provide nice error messages
    #Trap specific exceptions where possible

        #ValueError - int("NO")/if remove() does not find the value
        #TypeError - len(42) #wrong datatype for a parameter in a function
        #ZeroDivisionError - 1/0
        #NameError - print(answer) #no variable called answer
        #IndexError - index not in the list

#validation loops
#keep looping until the user enters an integer
# while True:
#     try:
#         user_input = int(input("Enter an integer: "))
#         break
#     except ValueError:
#         print("That is not an integer! Try again!")

#keep looping until they enter an integer between 1 and 10
#show the user_input in both error messages
while True:
    try:        
        user_input = input("Enter an integer: ")
        user_input = int(user_input)
        if user_input >=1 and user_input <=10:
            break#Exit the loop because the data is good!
        else:
            print(f"{user_input} is not valid! Must be between 1 and 10!")
    except ValueError:
        print(f"({user_input}) is not an integer! Try again!")


#Validation Loop Summary 
#Try the operation that could cause an exception
#If it explodes, catch it in the except
#If it works, escape the loop


#For assignment you could use Try/Except(But there may be other ways):
    #Casting to int errors on user input
    #remove()
    #invalid indexes
    