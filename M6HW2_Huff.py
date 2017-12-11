#Random Number Guessing Game
#CTI-110
#Jesse Huff
#10/30/2017

#import random
import random

#get the random number
def generate_random_number():
    randomNumber = random.randint(1,100)
    return randomNumber

#get user input
def guess_number(message = "Guess the number: "):
    user_input = int(input(message))
    return user_input

#check user input
def check_user_input(user_input, randomNumber):
    if user_input > randomNumber:
        print("Too High, Try again")
        return False
    elif user_input < randomNumber:
        print("Too Low, Try again")
        return False
    else:
        print("Congrats! You guessed the number!")
        return True

# number of guesses
def main():
    userNumberOfGuesses = 1
    randNumber = generate_random_number()
    won = False
    while(won == False):
        userInput = guess_number()
        if check_user_input(userInput,randNumber):
            won = True
            print("You Won in " + str(userNumberOfGuesses) + " guesses")
        else:
            userNumberOfGuesses+= 1
    while(True):
        getUserInput = input("Do you want to play again? (Y or N)")  #Play again feature
        if getUserInput.lower() == "y":
            main()
        elif getUserInput.lower() == "n":
            exit()
        
            
            

main()

        
