# 1 Define a function max() that takes two numbers as arguments and returns the largest of them. Use the if-then-else construct available in Python. (It is true that Python has the max() 

def max(one, two):
	if one > two:
		return one
	else:
		return two

print(max(2,3))

# 2 Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.

def max_of_three(one, two, three):
	return max(max(one, two), three)

print(max_of_three(1,2,3))

# 3 Define a function that finds the length of a given list or string. ( It is true that Python has the len() function built in, but writing it yourself is nevertheless a good exercise ).

def length(list):
	length = 0
	while list:
		length += 1
		list = list[0:-1]
	return length

print(length([1,2]))

# 4 Write a function that takes a character ( i.e. a string of length 1 ) and returns True if it is a vowel, False otherwise.

def vowel(letter):
	return letter in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

print(vowel('a'))

# 5 Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's language"). That is, double every consonant and place an occurrence of "o" in between. For example, translate("this is fun") should return the string "tothohisos isos fofunon".

def translate(text):
	translated_text = ''
	for letter in text:
		if vowel(letter) or letter == ' ':
			translated_text += letter
		else:
			translated_text += letter + 'o' + letter
	return translated_text

print(translate('felix'))

# 6 Define a function sum() and a function multiply() that sums and multiplies (respectively) all the numbers in a list of numbers. For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24.

def sum(numbers):
	sum = 0
	for number in numbers:
		sum += number
	return sum

def multiply(numbers):
	product = 1
	for number in numbers:
		product *= number
	return product

print(sum([1,2,3]))
print(multiply([1,2,3]))

# 7 Define a function reverse() that computes the reversal of a string. For example, reverse( "I am testing" ) should return the string "gnitset ma I".

def reverse(string):
	reversed_string = ''
	for letter in string:
		reversed_string += string[-1]
		string = string[0:-1]
	return reversed_string

print(reverse('felix'))

# 8 Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards). For example, is_palindrome( "radar" ) should return True.

def is_palindrome(text):
	return text == reverse(text)

print(is_palindrome('asdfdsa'))
print(is_palindrome('felix'))

# 9 Write a function is_member() that takes a value ( i.e. a number, string, etc ) x and a list of values a, and returns True if x is a member of a, False otherwise. (Note that this is exactly what the in operator does, but for the sake of the exercise you should pretend Python did not have this operator).

def is_member(number, list):
	for i in list:
		if i == number:
			return True
		else
			return False
# 10 Define a function overlapping() that takes two lists and returns True if they have at least one member in common, False otherwise. You may use your is_member() function, or the in operator, but for the sake of the exercise, you should (also) write it using two nested for-loops.
def overlapping(list1, list2):
	for i in list1:
		if is_member(i, list2)
			return True
		else
			return False
# 11 Define a function generate_n_chars() that takes an integer n and a character c and returns a string, n characters long, consisting only of c:s. For example, generate_n_chars( 5,"x" ) should return the string "xxxxx". (Python is unusual in that you can actually write an expression 5 * "x" that will evaluate to "xxxxx". For the sake of the exercise you should ignore that the problem can be solved in this manner ).
def generate_n_chars(number, letter):
	string = ''
	string += letter * number
	return string
# 12 Define a procedure histogram() that takes a list of integers and prints a histogram to the screen. For example, histogram( [ 4, 9, 7 ] ) should print the following:
def histogram(list_of_integers):
	for number in list_of_integers:
	string = (number, *)

# 16 Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n.

def filter_long_words(list, length):
	if length(list) > n:
		return list

print(filter_long_words("list", 2))
# 17 Write a version of a palindrome recognizer that also accepts phrase palindromes such as "Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis", "Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas", "I roamed under it as a tired nude Maori", "Rise to vote sir", or the exclamation "Dammit, I'm mad!". Note that punctuation, capitalization, and spacing are usually ignored.

def is_palindrome2(text):
	cleaned_text = ""
	for character in text.lower():
		if character.isalpha():
			cleaned_text += character
	return is_palindrome(cleaned_text)

print(is_palindrome2("Go hang a salami I'm a lasagna hog."))

# 18 A pangram is a sentence that contains all the letters of the English alphabet at least once, for example: "The quick brown fox jumps over the lazy dog". Your task here is to write a function to check a sentence to see if it is a pangram or not.

def pan(list):
	splitted_list = list.split

	for letter in splitted_list:
		

# 19 "99 Bottles of Beer" is a traditional song in the United States and Canada. It is popular to sing on long trips, as it has a very repetitive format which is easy to memorize, and can take a long time to sing. The song's simple lyrics are as follows:
#  Take one down, pass it around, 98 bottles of beer on the wall.```
#The same verse is repeated, each time with one fewer bottle. The song is completed when the singer or singers reach zero. Your task here is write a Python program capable of generating all the verses of the song.

def song():
	number_of_bottles = 99
	song = ''
	while number_of_bottles > 0:
		number_of_bottles -= 1
		song += 'Take one down, pass it around, {number_of_bottles} bottles of beer on the wall.'

	return song

# 20 Represent a small bilingual lexicon as a Python dictionary in the following fashion

#{ "merry":"god", "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"år" }

#and use it to translate your Christmas cards from English into Swedish. That is, write a function `translate()` that takes a l

def translate(word):
	dictionary = { "merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år" }
	return dictionary[word]

#21. Write a function `char_freq()` that takes a string and builds a frequency listing of the characters contained in it. Represent the frequency listing as a Python dictionary. Try it with something like `char_freq("abbabcbdbabdbdbabababcbcbab")`.

def char_freq(list):
	for char in list:

#23. Define a simple "spelling correction" function `correct()` that takes a string and sees to it that 1) two or more occurrences of the space character is compressed into one, and 2) inserts an extra space after a period if the period is directly followed by a letter. E.g. `correct("This   is  very funny  and    cool.Indeed!")` should return "This is very funny and cool. Indeed!" Tip: Use regular expressions!

def correct(string):
	corrected = " "
	for char in string:
		if char.is_alpha:
			corrected += char

#24. The third person singular verb form in English is distinguished by the suffix -s, which is added to the stem of the infinitive form: run -> runs. A simple set of rules can be given as follows:

#a. If the verb ends in y, remove it and add ies
#b. If the verb ends in o, ch, s, sh, x or z, add es
#c. By default just add s
#Your task in this exercise is to define a function `make_3sg_form()` which given a verb in infinitive form returns its third person singular form. Test your function with words like try, brush, run and fix. Note however that the rules must be regarded as heuristic, in the sense that you must not expect them to work for all cases. Tip: Check out the string method `endswith()`.

def make_3sg_form(verb):
	new_verb = ' '
	verbbb = verb.split():
	if verbbb[-1] == y
		new_verb = verb[0..-1]  + ies
	elif verbbb[-1] == o or ch or  s or sh or x or z:
		new_verb = verb[0..-1]  + es
	else new_verb = verb[0..-1]  + s
	return new_verb
	
# 25. In English, the present participle is formed by adding the suffix -ing to the infinite form: go -> going. A simple set of heuristic rules can be given as follows:

# 1. If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.)
# 2. If the verb ends in ie, change ie to y and add ing
# 3. For words consisting of consonant-vowel-consonant, double the final letter before adding ing
# 4. By default just add ing

# Your task in this exercise is to define a function `make_ing_form()` which given a verb in infinitive form returns its present participle form. Test your function with words such as lie, see, move and hug. However, you must not expect such simple rules to work for all cases.

def make_ing_form(verb):
	split = verb.split()
	if split[-1] = e
		return split[0..-2] + 'ing'
	elif split[-1] = ie
		return split[0..-2] + 'ying'
	else split[-1]  NOT IN ['a', 'e', 'i', 'o', 'u'], split[-2] IN ['a', 'e', 'i', 'o', 'u'], split[-3] NOT IN ['a', 'e', 'i', 'o', 'u']
		return split[0..-2] + split[-1] + split[-1] + 'ing'

# 26. Using the higher order function `reduce()`, write a function `max_in_list()` that takes a list of numbers and returns the largest one. Then ask yourself: why define and call a new function, when I can just as well call the `reduce()` function directly?

def max_in_list(list):
	max = 0
	for number in list:
		if number >= max
			max = number
	return max

# 27. Write a program that maps a list of words into a list of integers representing the lengths of the corresponding words. Write it in three different ways: 1) using a for-loop, 2) using the higher order function `map()`, and 3) using list comprehensions.

def change(list):
	length = ''
		for word in list:
			split = word.split()
			length += split.count
	return length

# 28. Write a function `find_longest_word()` that takes a list of words and returns the length of the longest one. Use only higher order functions.
def find_longest_word(list):
	longest = ''
	for word in list:
		split = word.split()
		if split.count >= longest
			longest = word
	return longest

# 29. Using the higher order function `filter()`, define a function `filter_long_words()` that takes a list of words and an integer n and returns the list of words that are longer than n.


# 30. Represent a small bilingual lexicon as a Python dictionary in the following fashion {"merry":"god", "christmas":"jul", "and":"o

def translate(word):
	dictionary = { "merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år" }
	return dictionary[word]

# 31. Implement the higher order functions `map()`, `filter()` and `reduce()`. (They are built-in but writing them yourself may be a good exercise.)

def my_map(list, function):
	new_list = []
	for element in list:
		new_list.append(function(element))
	return new_list

def my_filter(list, function):
	new_list = []
	for element in list:
		if function(element):
			new_list.append(element)
	return new_list

def above_10(number):
	return number > 10

def my_reduce(list, accumulator, function):
	for element in list:
		accumulator = function(element, accumulator)
	return accumulator

def add(number, accumulator):
	return number + accumulator

def subtract(number, accumulator):
	return accumulator - number

my_reduce([1,2,3,4], 0, add)
my_filter([1,5,20,30], above_10)
# 32. Write a version of a palindrome recognizer that accepts a file name from the user, reads each line, and prints the line to the screen if it is a palindrome.

def asdf(file):
	return is_palindrome(file)
# 33. According to Wikipedia, a semordnilap is a word or phrase that spells a different word or phrase backwards. ("Semordnilap" is itself "palindromes" spelled backwards.) Write a semordnilap recognizer that accepts a file name (pointing to a list of words) from the user and finds and prints all pairs of words that are semordnilaps to the screen. For example, if "stressed" and "desserts" is part of the word list, the the output should include the pair "stressed desserts". Note, by the way, that each pair by itself forms a palindrome!

# 34. Write a procedure `char_freq_table()` that, when run in a terminal, accepts a file name from the user, builds a frequency listing of the characters contained in the file, and prints a sorted and nicely formatted character frequency table to the screen.

# 35. The International Civil Aviation Organization (ICAO) alphabet assigns code words to the letters of the English alphabet acrophonically (Alfa for A, Bravo for B, etc.) so that critical combinations of letters (and numbers) can be pronounced and understood by those who transmit and receive voice messages by radio or telephone regardless of their native language, especially when the safety of navigation or persons is essential. Here is a Python dictionary covering one version of the ICAO alphabet:

# Your task in this exercise is to write a procedure `speak_ICAO()` able to translate any text (i.e. any string) into spoken ICAO words. You need to import at least two libraries: os and time. On a mac, you have access to the system TTS (Text-To-Speech) as follows: `os.system('say ' + msg)`, where msg is the string to be spoken. (Under UNIX/Linux and Windows, something similar might exist.) Apart from the text to be spoken, your procedure also needs to accept two additional parameters: a float indicating the length of the pause between each spoken ICAO word, and a float indicating the length of the pause between each word spoken.

# 36. A hapax legomenon (often abbreviated to hapax) is a word which occurs only once in either the written record of a language, the works of an author, or in a single text. Define a function that given the file name of a text will return all its hapaxes. Make sure your program ignores capitalization.

# 37. Write a program that given a text file will create a new text file in which all the lines from the original file are numbered from 1 to n (where n is the number of lines in the file).

def line_in_file(file):
	file = open("gfg.txt","r")
	Counter = 0
	

	Content = file.read()
	CoList = Content.split("\n")
	
	for i in CoList:
		if i:
			Counter += 1

print(Counter)
# 38. Write a program that will calculate the average word length of a text stored in a file (i.e the sum of all the lengths of the word tokens in the text, divided by the number of word tokens).
def average_length(sentence):
	words = sentence.split()
	average = sum(len(word) for word in words) / len(words)
	return average

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

def guess_the_number():
	print("Hello! What is your name?")
	input()


guess_the_number()
# 40. An anagram is a type of word play, the result of rearranging the letters of a word or phrase to produce a new word or phrase, using

#  all the original letters exactly once; e.g., orchestra = carthorse, A decimal point = I'm a dot in place. Write a Python program that,
#  
# when started 1) randomly picks a word w from given list of words, 2) randomly permutes w (thus creating an anagram of w), 3) presents 

# the anagram to the user, and 4) enters an interactive loop in which the user is invited to guess the original word. It may be a good 

# idea to work with (say) colour words only. The interaction with the program may look like so:

# import anagram Colour word anagram: onwbr Guess the colour word! black Guess the colour word! brown Correct!

