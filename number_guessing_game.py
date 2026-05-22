#number guessing game
#user has to guess the correct number

import random

#generating random number

secret = random.randint(1,10)

guess = 0

print("guess a number between 1 to 10")


#loop until user guesses correctly

while guess != secret:

    guess = int(input("enter your guess: "))

    if guess < secret:
        print("too low")

    elif guess > secret:
        print("too high")

    else:
        print("correct guess")