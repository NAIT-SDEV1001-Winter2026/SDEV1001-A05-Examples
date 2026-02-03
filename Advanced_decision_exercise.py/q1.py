# 1.	Create a file named heads_or_tails.py in this folder. Write a program that lets the user guess whether the flip of a coin results in heads or tails. The program randomly generates an integer 0 to 1, which represents heads or tails. The program prompts the user to enter a guess and reports whether the guess is correct or incorrect.
# a.	import the random module to generate a random numbers
# b.	use random.randint(0, 1) to generate a random number between 0 and 1
import random

#heads will be 0 and tails will be 1
random_number = random.randint(0,1)

user_guess = input("Guess the coin flip! Enter heads or tails (h/t): ")

#Display coin flip
if random_number == 0:
    print("The coin flip was: heads")
else:
    print("The coin flip was: tails")

#Compare flip to guess and display message
if ((random_number == 0 and user_guess == "h")
    or (random_number == 1 and user_guess == "t")):
    print("you guessed correct!")
else:
    print("you guessed wrong!")