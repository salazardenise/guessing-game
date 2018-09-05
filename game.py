"""A number-guessing game."""
from random import randint

# Put your code here
print ("Howdy, what's your name?")
name = input ("(type in your name) ")

print ("{}, I'm thinking of a number between 1 and 100.".format(name))
print ("Try to guess my number.")

num = randint(1,100)
tries = 0

while True:
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
        print ("Your guess in too high, try again.")

print ("Well done, {}! You found my number in {} tries!".format(name, tries))