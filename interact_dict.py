#import library
import json

#Loading the json data as python dictionary
data = json.load( open("data.json") )

def retrieve_definition(word):
	if word in data:
		return data[word]
	else:
		return ("The word doesn't exist , please double check it")

#input from user
user_word = input('Enter word : ')

print(retrieve_definition(user_word))
	
