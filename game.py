"""A number-guessing game."""
from random import randint

# Put your code here
print ("Howdy, what's your name?")
name = input ("(type in your name) ")
playAgain = 'yes'
bestScore = None
try:
    maxTries = int(input("What\'s the maximum number of guesses you need per round? "))
except ValueError:
    print("That wasn't a valid number.  You get 20 tries.")
    maxTries=20


while playAgain == 'yes':
    print ("{}, I'm thinking of a number between 1 and 100.".format(name))
    print ("Try to guess my number.")

    num = randint(1,100)
    tries = 0

    while tries < maxTries:
        try:
            guess = int(input("Your guess? ")) 
        except ValueError: 
            print ("That wasn't a valid number. Try again")
            continue
            
        # check for valid input
        if guess < 1 or guess > 100:
            print("You have committed a crime. Please enter a number between 1 and 100")
            continue

        tries += 1
        if num == guess:
            break
        elif num > guess:
            print("Your guess is too low, try again.")
        else:
            print("Your guess in too high, try again.")

    if tries >= maxTries:
        print("Too many tries.  The number was {}.   :-( ".format(num))
    else:
        print("Well done, {}! You found my number in {} tries!".format(name, tries))
        if bestScore is None or tries < bestScore:
            bestScore = tries
        # print ("bestScore so far is {}".format(bestScore))

    playAgain = input("Would you like to play again? (enter Yes to play again):  ")
    playAgain = playAgain.lower()

if bestScore is None:
    print ("Thanks for playing! You didn't win any games today.")
else: 
    print ("Thanks for playing! Your best score today was {} guesses. Bye.".format(bestScore))
