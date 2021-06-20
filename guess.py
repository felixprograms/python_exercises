# 39. Write a program able to play the "Guess the number"-game, where the number to be guessed is randomly chosen between 1 and 20. (Source: http://inventwithpython.com) This is how it should work when run in a terminal:

# import guess_number Hello! What is your name? Torbjörn Well, Torbjörn, I am thinking of a number between 1 and 20. Take a guess. 10 Your guess is too low. Take a guess. 15 Your guess is too low. Take a guess. 18 Good job, Torbjörn! You guessed my number in 3 guesses!

# Hello! What is your name?
# Albert
# Well, Albert, I am thinking of a number between 1 and 20.
# Take a guess.
# 10
# Your guess is too high.
# Take a guess.
# 2
# Your guess is too low.
# Take a guess.
# 4
# Good job, Albert! You guessed my number in 3 guesses!
import random
def guess_the_number():
    print("Hello! What is your name?")
    player_name = input()
    print(f'Well, {player_name}, I am thinking of a number between 1 and 20.')
    random_number = random.randint(1,20)
    number_of_guesses = 0
    guess = None
    while guess is not random_number:
        number_of_guesses += 1
        print("Take a guess.")
        guess = int(input())
        if guess > random_number:
            print("Your guess is too high.")
        elif guess < random_number:
            print("Your guess is too low.")
        else:
            print(f'Good job, {player_name}! You guessed my number in {number_of_guesses} guesses!')

        

# guess_the_number()

# 40. An anagram is a type of word play, the result of rearranging the letters of a word or phrase to produce a new word or phrase, using

#  all the original letters exactly once; e.g., orchestra = carthorse, A decimal point = I'm a dot in place. Write a Python program that,
#  
# when started 
# 1) randomly picks a word w from given list of words, 
# 2) randomly permutes w (thus creating an anagram of w),
#  3) presents the anagram to the user, and 
# 4) enters an interactive loop in which the user is invited to guess the original word. It may be a good idea to work with (say) colour 
# words only. The interaction with the program may look like so:

# import anagram Colour word anagram: onwbr Guess the colour word! black Guess the colour word! brown Correct!

def guess_the_colour():
    colours = ['red', 'blue', 'yellow', 'green', 'white', 'brown']
    random_colour = colours[random.randint(0,5)]
    splited_colour = list(random_colour)
    random.shuffle(splited_colour)
    new_random_colour = ''.join(splited_colour)
    guess = None
    print(f'{new_random_colour}')
    print("Guess the colour.")
    while guess is not random_colour:
        guess = input()
        print(guess)
        print(random_colour)
        if guess == random_colour:
            print("Correct!")
            break
        else:
            print("Guess Again")

guess_the_colour()
