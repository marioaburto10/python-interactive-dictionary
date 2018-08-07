# importing my dependencies
import json
from difflib import get_close_matches 

# using the json load() function to open and load the data.json file
# data is a dictionary
data = json.load(open("./Resources/data.json"));

# a function that takes in a word as a string and returns that word's definition if it is in the data.json file 
def translate(word): 
	# turns the user's word to all lowercase letters just incase the urser uses a micture of upercase and lower case letters
	word = word.lower()
	# an if statement that checks if the word does exist in the dictioany in data.json
	# if the word does exist in the dictionary, return its definition

	if word in data:
		return data[word]
	# if the word is not the data.json file, then sue the get_close_matches function from difflib to check for any similar words
	elif len(get_close_matches(word, data.keys())) > 0:
		answer = input("Did you mean %s instead? Enter Y for yes or N for no: " % get_close_matches(word, data.keys())[0])
		answer = answer.lower()


		if answer == "" or answer[0] == 'y':
			recomended_word = get_close_matches(word, data.keys())[0]
			return data[recomended_word]
		elif answer[0] == "n":
			return "Sorry, no matches found. Please try another word"
		
	# else return a string saying it does not exist
	else:
		return "Word does not exist in this dictionary, please try another word"

# will ask the user to input a word and it will be stored in the variable called word
word = input("Enter a word that you want a definition for: ") 

print(translate(word)) # if word = "hello", it will return ['Expression of greeting used by two or more people who meet each other.']