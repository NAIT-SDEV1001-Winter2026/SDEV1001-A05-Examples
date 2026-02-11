import random

play = "y"
while play == "y":
    guesses = 0
    #Generate a random number between 1 and 100
    random_number = 5#random.randint(1,100)
    is_done = False
    while not is_done:
    #get the guess from the user
        guess = int(input("Enter a number between 1 and 100: "))
        #determine too high or too low or win
        guesses += 1
        if guess == random_number:
            #win
            print("You win!")  
            is_done = True 
        elif guess < random_number:
            #Too Low
            print("Too low!")
        else:
            #Too High
            print("Too high!")

    #if win print how many guesses
    print(f"It took you {guesses} guesses")
    is_valid = False
    play = input("Would you like to play again? (y/n): ")
    while not is_valid:        
        if play == "y" or play == "n":
            is_valid = True
        else:
            play = input(f"Invalid entry! Cannot be {play}! Read the rules! Would you like to play again? (y/n): ")
            
#Add on logic to allow the user to play again (if they want) after they win




