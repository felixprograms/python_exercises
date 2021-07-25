# 41. In a game of Lingo, there is a hidden word, five characters long. The object of the game is to find this word by guessing, 
# and in return receive two kinds of clues: 1) the characters that are fully correct, with respect to identity as well as to position, 
# and 2) the characters that are indeed present in the word, but which are placed in the wrong position. Write a program with which one 
# can play Lingo. Use square brackets to mark characters correct in the sense of 1), and ordinary parentheses to mark characters correct 
# in the sense of 2). Assuming, for example, that the program conceals the word "tiger", you should be able to interact with it in the 
# following way:

# import lingo snake Clue: snak(e) fiest Clue: fis(t) times Clue: [t][i]m[e]s tiger Clue: [t][i][g][e][r]

# def lingo(word):
#     guess = ''
#     while word != guess:
#         dictionary = {}
#         guess = input()
#         print(guess)
#         for letter in word:
#             if letter in dictionary:
#                 dictionary[letter] += 1
#             else:
#                 dictionary[letter] = 1
#         hint = ''
#         for i in range(len(word)):
#             if word[i] == guess[i]:
#                 dictionary[word[i]] -= 1
#         for i in range(len(word)):
#             if word[i] == guess[i]:
#                 hint += '['
#                 hint += word[i]
#                 hint += ']'
#                 dictionary[word[i]] -= 1
#             elif guess[i] in dictionary and dictionary[guess[i]] > 0:
#                 hint += '('
#                 hint += guess[i]
#                 hint += ')'
#                 dictionary[guess[i]] -= 1
#             else:
#                 hint += guess[i]

#         print(hint)



# 42. A sentence splitter is a program capable of splitting a text into sentences. The standard set of heuristics for sentence 
# splitting includes (but isn't limited to) the following rules:
# Sentence boundaries occur at one of "." (periods), "?" or "!", except that
# 1. Periods followed by whitespace followed by a lower case letter are not sentence boundaries.
# 2. Periods followed by a digit with no intervening whitespace are not sentence boundaries.
# 3. Periods followed by whitespace and then an upper case letter, but preceded by any of a short list of titles are not sentence 
# boundaries. Sample titles include Mr., Mrs., Dr., and so on.
# 4. Periods internal to a sequence of letters with no adjacent whitespace are not sentence boundaries (for example, www.aptex.com,
#  or e.g).
# 5. Periods followed by certain kinds of punctuation (notably comma and more periods) are probably not sentence boundaries.
# 6. Your task here is to write a program that given the name of a text file is able to write its content with each sentence on a 
# separate line. Test your program with the following short text:
# Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it. Did he mind? Adam Jones Jr. thinks he didn't.
#  In any case, this isn't true... Well, with a probability of .9 it isn't.
# The result should be:
# Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it. Did he mind? Adam Jones Jr. thinks he didn't. 
# In any case, this isn't true... Well, with a probability of .9 it isn't.
    
# 43. An anagram is a type of word play, the result of rearranging the letters of a word or phrase to produce a new word or phrase, 
# using all the original letters exactly once; e.g., orchestra = carthorse. Using the word list at
#  http://wiki.puzzlers.org/pub/wordlists/unixdict.txt, write a program that finds the sets of words that share the same 
# characters that contain the most words in them.

with open('unixdict.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 


def anagram():
    dictionary = {}

    for word in content:
        letters = list(word)
        letters.sort()
        sorted_word = ''.join(letters)
        if sorted_word in dictionary:
            dictionary[sorted_word].append(word)
        else:
            dictionary[sorted_word] = [word]

    all_groups = [value for key, value in dictionary.items()]
    length_of_longest_group = None
    longest_group = None
    for group in all_groups:
        if length_of_longest_group == None or len(group) > length_of_longest_group:
            length_of_longest_group = len(group)
            longest_group = group
    
    print(longest_group)
        
# anagram()

anagram()
# 44. Your task in this exercise is as follows:

# Generate a string with N
# 
# generated string is balanced; that is, whether it consists entirely of pairs of opening/closing brackets (in 
# that order), none of which mis-nest.
# Examples:

#  []        OK   ][        NOT OK
#  [][]      OK   ][][      NOT OK
#  [[][]]    OK   []][[]    NOT OK

def balanced_string(string):
    new_list = []
    for bracket in string:
        if bracket == '[':
            new_list.append(bracket)
        elif bracket == ']' and len(new_list) > 0:
            new_list.pop()
        else:
            return "Unbalanced"
    
    if len(new_list) == 0:
        return "Balanced"
    else:
        return "Unbalanced"

balanced_string('][')
# 45. A certain children game involves starting with a word in a particular category. Each participant in turn says a word, but that 
# word must begin with the final letter of the previous word. Once a word has been given, it cannot be repeated. If an opponent cannot
#  give a word in the category, they fall out of the game. For example, with "animals" as the category,

# Child 1: dog Child 2: goldfish Child 1: hippopotamus Child 2: snake ...


# Your task in this exercise is as follows: Take the following selection of 70 English Pokemon names (extracted from Wikipedia's list 
# of Pokemon) and generate the/a sequence with the highest possible number of Pokemon names where the subsequent name starts with the 
# final letter of the preceding name. No Pokemon name is to be repeated.


pokemons = ["audino","bagon","baltoy","banette","bidoof","braviary","bronzor","carracosta","charmeleon","cresselia","croagunk","darmanitan","deino","emboar","emolga","exeggcute","gabite","girafarig","gulpin","haxorus","heatmor","heatran","ivysaur","jellicent","jumpluff","kangaskhan","kricketune","landorus","ledyba","loudred","lumineon","lunatone","machamp","magnezone","mamoswine","nosepass","petilil","pidgeotto","pikachu","pinsir","poliwrath","poochyena","porygon2","porygonz","registeel","relicanth","remoraid","rufflet","sableye","scolipede","scrafty","seaking","sealeo","silcoon","simisear","snivy","snorlax","spoink","starly","tirtouga","trapinch","treecko","tyrogue","vigoroth","vulpix","wailord","wartortle","whismur","wingull","yamask"]

class PokemonNode:
	def __init__(self, value, parent = None):
		self.value = value
		self.parent = parent
		self.children = []
	def insert(self, pokemon):
		node = PokemonNode(pokemon, self)
		self.children.append(node)

trees = []

for pokemon in pokemons[:10]:
	root = PokemonNode(pokemon)
	trees.append(root)
	queue = [root]
	while queue != []:
		current_node = queue[0]
		queue = queue[1:]
		ancestral_node = current_node
		ancestors = {}
		while ancestral_node != None:
			ancestors[ancestral_node.value] = True
			ancestral_node = ancestral_node.parent
		for pokemon in pokemons:
			if pokemon not in ancestors and current_node.value[-1] == pokemon[0]:
				current_node.insert(pokemon)
		queue += current_node.children

print(trees)
print(game(pokemons))
# 46. An alternade is a word in which its letters, taken alternatively in a strict sequence, and used in the same order as the original
#  word, make up at least two other words. All letters must be used, but the smaller words are not necessarily of the same length. For 
# example, a word with seven letters where every second letter is used will produce a four-letter word and a three-letter word. Here are 
# two examples:

# "board": makes "bad" and "or".
# "waists": makes "wit" and "ass".
# Using the word list at http://www.puzzlers.org/pub/wordlists/unixdict.txt, write a program that goes through each word in the list and 
# tries to make two smaller words using every second letter. The smaller words must also be members of the list. Print the words to the 
# screen in the above fashion.

