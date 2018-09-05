"""A number-guessing game."""
from random import randint

# Put your code here
print ("Howdy, what's your name?")
name = input ("(type in your name) ")

print ("{}, I'm thinking of a number between 1 and 100.".format(name))
print ("Try to guess my number")

num = randint(1,100)
tries = 0

while True:
    tries += 1
    guess = int(input("Your guess? ")) 
    # print(num)
    if num == guess:
        break
    elif num > guess:
        print("Your guess is too low, try again.")
    else:
        print ("Your guess in too high, try again.")

print ("Well done, {}! You found my number in {} tries!".format(name, tries))