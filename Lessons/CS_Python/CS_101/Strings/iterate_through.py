# Write a new function called get_length() that takes a string as an input and returns the number of characters in that string.

def get_length(word):
    counter = 0
    for letter in word:
        counter += 1
    return counter

