# 3.	Create a file named rock_paper_scissors.py in this folder. Write a program that plays the scissor-rock-paper game. (A scissor cuts paper, a rock can crush a scissor, and a paper can cover a rock.) The program randomly generates a number 0, 1, or 2 representing scissor, rock, and paper. The program prompts the user to enter a number 0, 1, or 2 and displays a message indicating whether the user or the computer wins, loses, or draws.

import random

result = "You lose"

#Get user input and generate a random number between 0 and 2
user_input =  int(input("Scissor (0), rock (1), paper (2): "))
computer_input = random.randint(0, 2)

#Translate the user input integer to a string word
if user_input == 0:
    user_result = "scissor"
elif user_input == 1:
    user_result = "rock"
elif user_input == 2:
    user_result = "paper"

#Translate the computer integer to a string word
if computer_input == 0:
    computer_result = "scissor"
elif computer_input == 1:
    computer_result = "rock"
elif computer_input == 2:
    computer_result = "paper"

#tie
if user_result == computer_result:
    result = "It is a draw"
#user wins 
elif ((user_result == "paper" and computer_result == "rock") or 
      (user_result == "rock" and computer_result == "scissor") or
      (user_result == "scissor" and computer_result == "paper")):
    result = "You win"
# else:
#     result = "You lose"

print(f"The computer is {computer_result}. You are {user_result}.{result}")