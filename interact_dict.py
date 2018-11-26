#import library
import json
import difflib
from difflib import get_close_matches

#Loading the json data as python dictionary
data = json.load( open("data.json") )

def retrieve_definition(word):
	#Removing case sensitivity of the program
	word = word.lower()
	
	#Check for non existing words
    #1st elif: To make sure the program return the definition of words that start with a capital letter (e.g. Delhi, Texas)
    #2nd elif: To make sure the program return the definition of acronyms (e.g. USA, NATO)
	if word in data:
		return data[word]
	elif word.title() in data:
		return data[word.title()]
	elif word.upper() in data:
		return data[word.upper()]
	#3rd elif: To find a similar word
	#-- len > 0 because we can print only when the word has 1 or more close matches
	#-- In the return statement, the last [0] represents the first element from the list of close matches
	elif len(get_close_matches(word, data.keys())) > 0:
		closed_match = get_close_matches(word , data.keys())[0]
		action = input('Did you mean %s instead? [y or n]: ' %  closed_match)
    	#-- If the answers is yes, retrive definition of suggested word
		if action == 'y':
			return data[closed_match]
		elif action == 'n':
			return ("The word doesn't exist, yet.")
		else:
			return ("We don't understand your entry. Apologies.")

#input from user
user_word = input('Enter word : ')

print(retrieve_definition(user_word))
	
