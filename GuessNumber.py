#-------------------------------------------------------------------------------
# Name:        Guess the Number Game
# Purpose:     
#
# Author:      xchido
#
# Created:     20140314
# Copyright:   (c) xchido 2014
# Licence:     CC0
#-------------------------------------------------------------------------------

# This is a guess the number game.

import random
guessesTaken = 0
print('Hello! What is your name?')
myName = input("Enter Name: ")
number = random.randint(1, 1005)
print('Well, ' + myName + ', I am thinking of a number between 1 and 100.')
while guessesTaken < 6:
    # print('Take a guess: ') # There are four spaces in front of print.
    guess = input("Wanna Play? Take a guess: ")
    guess = int(guess)
    guessesTaken = guessesTaken + 1
    if guess < number:
        print('Wrong, your guess is too low. Try again: ') # There are eight spaces in front of print.
    if guess > number:
        print('Wrong, your guess is too high. Try again: ')
    if guess == number:
        break
if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')
if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was: ' + number)