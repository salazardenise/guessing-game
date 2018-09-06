"""A number-guessing game."""
from random import randint

def getNum(prompt, start=None, end=None):
    try:
        num=int(input(prompt))
    except ValueError:
        print("Invalid number.")
        num = None

    if start is not None:
        if num < start:
            print ("Number must be greater than {}".format(start))
            num = None

    if end is not None:
        if num > end:
            print ("Number must be less than {}".format(end))
            num = None
    return num


def playGame(maxTries, start, end):
    print("{}, I'm thinking of a number between {} and {}.".format(name, start, end))
    print("Try to guess my number.")

    num = randint(start,end)
    tries = 0

    while tries < maxTries:
        guess = getNum("Your guess? ", start, end)
        if guess is None:
            print("Try again. Enter a number between {} and {}".format(start, end))
            continue
        '''
        try:
            guess = int(input("Your guess? ")) 
        except ValueError: 
            print("That wasn't a valid number. Try again")
            continue
        '''

        # check for valid input
        '''
        if guess < start or guess > end:
            print("You have committed a crime. Please enter a number between {} and {}".format(start, end))
            continue
        '''

        tries += 1
        if num == guess:
            break
        elif num > guess:
            print("Your guess is too low, try again.")
        else:
            print("Your guess in too high, try again.")

    if tries >= maxTries:
        print("Too many tries.  The number was {}.   :-( ".format(num))
        return None
    else:
        print("Well done, {}! You found my number in {} tries!".format(name, tries))
        return tries


def scoreGame(tries, start, end):
    if tries is None:
        score = 0
    else:
        rangeSize = end - start
        score = rangeSize // tries
    print("Your score is {}".format(score))
    return score


# Put your code here
print("Howdy, what's your name?")
name = input("(type in your name) ")


# Get the range of valid guesses
'''
try:
    start = int(input("What's the start of the range? (enter starting number): "))
    end = int(input("What's the end of the range? (enter ending number): "))
except ValueError:
    print("Invalid range numbers. We'll use 1 to 100.")
'''
start = getNum("What's the start of the range? (enter starting number): ")
end = getNum("What's the end of the range? (enter ending number): ")
if start is None or end is None or start > end:
    print("Invalid range. We'll use 1 to 100")
    start = 1
    end = 100


try:
    maxTries = int(input("What\'s the maximum number of guesses you need per round? "))
except ValueError:
    print("That wasn't a valid number.  You get 20 tries.")
    maxTries=20

if maxTries < 1:
    print("Need a positive number.  You get 20 tries.")
    maxTries=20
    

playAgain = True
bestScore = 0

while playAgain:
    tries = playGame(maxTries, start, end)
    score = scoreGame(tries, start, end)
    if score > bestScore:
        bestScore = score
        # print ("bestScore so far is {}".format(bestScore))

    playAgainAnswer = input("Would you like to play again? (enter Yes to play again):  ")
    if playAgainAnswer.lower() != 'yes':
        playAgain = False
    
if bestScore == 0:
    print("Thanks for playing! You didn't win any games today.")
else: 
    print("Thanks for playing! Your best score today was {}. Bye.".format(bestScore))
