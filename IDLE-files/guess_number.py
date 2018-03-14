# Guess the number game.
# Save file as GuessNumber.
# Run the Module (or type F5).

import random # Import the random module.

num_guesses = 0
name = input('Hi! What is your name? ')
number = random.randint(1, 20) # A random integer between 1 and 20.
print('Welcome, {}! I am thinking of an integer between 1 and 20.'.format(name))

while num_guesses < 6:
    guess = int(input('Take a guess and type the integer? '))
    num_guesses += 1

    if guess < number:
        print('Your guess is too low.')
    if guess > number:
        print('Your guess is too high.')
    if guess == number:
        break

if guess == number:
    print('Well done {}! You guessed my number in {} guesses!'.format(name, num_guesses))
else:
    print('Sorry, you lose! The number I was thinking of was {}'.format(number))
