#Decision  making is basically the abiilty to control the flow of a program based on conditions
#In Python we will use if, elif, else

#Syntax of a basic if decision
#if condtion:
    #code to run of condition is True

# ==, !=, < , <=, > , >=

age = 14

if age >= 18:
    print ("You are an adult!")#only if age >=18
    print ("But you act like a child!")#only if age >=18

print ("Have a groovy day!")#always executes

#comparing equal values
name = input("Enter your name: ")

if name.upper() == "SHANE":
    print("Awesome Name!")

print(f"Have a groovy day {name.capitalize()}!")

#Boolean
#Use the word is in front of Boolean variables
is_awesome = False

if is_awesome == True:
    print ("That is awesome!")

#Boolean decsions should be written like this
if is_awesome:
    print ("That is awesome!")

#Checking for false
if not is_awesome:
    print ("That is NOT awesome!")

#if else
#if condition:
    #True code
#else:
    #False code

grade  = int(input("Enter a grade: "))
#with just if statments. BAD :( :(
if grade >= 50:
    print("Pass")
if grade < 50:
    print("Fail")

print("Have a groovy day!")
#GOOD WAY :) :)
if grade >= 50:
    print("Pass")
else:
    print("Fail")

print("Have a groovy day!")

#if elif else
grade  = int(input("Enter a grade: "))

if grade >= 80:
    print("Honors!")
    print("You are smart!")
elif grade >= 50:
    print ("Pass")
elif grade == 0:
    print ("Where ya been? Come to class!")
else: #catches anything not caught by the above conditions
    print ("Fail")



    

    




