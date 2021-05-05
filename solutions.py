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

# 10 Define a function overlapping() that takes two lists and returns True if they have at least one member in common, False otherwise. You may use your is_member() function, or the in operator, but for the sake of the exercise, you should (also) write it using two nested for-loops.


