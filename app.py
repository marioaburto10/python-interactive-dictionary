# importing my dependencies
import json

# using the json load() function to open and load the data.json file
# data is a dictionary
data = json.load(open("./Resources/data.json"));

# a function that takes in a word as a string and returns that word's definition if it is in the data.json file 
def translate(word): 
	# an if statement that checks if the word does exist in the dictioany in data.json
	# if the word does exist in the dictionary, return its definition
	# else return a string saying it does not exist
	if word in data:
		return data[word]
	else:
		return "word does not exist, please try another word"

# will ask the user to input a word and it will be stored in the variable called word
word = input("Enter a word that you want a definition for: ") 

print(translate(word)) # if word = "hello", it will return ['Expression of greeting used by two or more people who meet each other.']