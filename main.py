import json
from difflib import get_close_matches

data = json.load(open("data.json"))  # load the data from the json file


def translate(index):  # check if the word exist in the file
    index = index.lower()
    capitalize_index = index.capitalize()  # for nouns
    upper_index = index.upper()  # for acronyms
    if index in data:  # if the word exist in all lower case
        return data[index]
    if capitalize_index in data:  # if the word in a noun
        return data[capitalize_index]
    if upper_index in data:  # if the word is an acronyms
        return data[upper_index]
    elif len(get_close_matches(index, data.keys())) > 0:  # Return a list of the best “good enough” matches in order
        yon = input("Did you mean %s instead? Enter Y or N\n" % get_close_matches(index, data.keys())[0])
        if yon == "Y":
            return data[get_close_matches(index, data.keys())[0]]
        elif yon == "N":
            return "The word doesn't exist. Please double check it"
        else:
            return "we didn't understand your entry"
    else:
        return "The word doesn't exist. Please double check it"


word = input("Enter word : ")
meaning = translate(word)  # case sensitive
if type(meaning) == list:
    for i in meaning:  # printing all the available definitions
        print(i)
else:  # there's only 1 definition
    print(meaning)
