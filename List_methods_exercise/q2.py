import random

random_numbers = [random.randint(1,10), random.randint(1,10), random.randint(1,10)]
                  
print ("Welcome to the ultimate guessing game!")
guess = int(input("Enter a number to guess: "))

if guess in random_numbers:
    print ("You win!")
else:
    print("You lose!")

print (f"The numbers were: {random_numbers }")