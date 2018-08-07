# importing my dependencies
import json

# using the json load() function to open and load the data.json file
# data is a dictionary
data = json.load(open("./Resources/data.json"));

# a function that takes in a word as a string and returns that word's definition if it is in the data.json file 
def translate(word): 
	return data[word]

# will ask the user to input a word and it will be stored in the variable called word
word = input("Enter a word that you want a definition for: ") 

translate(word) # if word = "hello", it will return ['Expression of greeting used by two or more people who meet each other.']