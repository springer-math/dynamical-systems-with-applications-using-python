# Guess the number game.
# Save file as GuessNumber.

import random # Import the random module.

NumGuesses = 0
print('Hi! What is your name?')
Name = input()
number = random.randint(1, 20) # A random integer between 1 and 20.
print('Welcome, ' + Name + ', I am thinking of an integer between 1 and 20.')
while NumGuesses < 6:
    print('Take a guess and type the integer?') 
    guess = input()
    guess = int(guess)
    NumGuesses  = NumGuesses + 1
    
    if guess < number:
        print('Your guess is too low.') 

    if guess > number:
        print('Your guess is too high.')
        
    if guess == number:
        break
    
if guess == number:
    NumGuesses  = str(NumGuesses )
    print('Well done ' + Name + '! You guessed my number in ' +
          NumGuesses  + ' guesses!')

if guess != number:
    number = str(number)
    print('Sorry, you lose! The number I was thinking of was ' + number)
