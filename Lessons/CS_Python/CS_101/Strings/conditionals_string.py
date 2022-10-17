# Write a function called letter_check that takes two inputs, word and letter.

# This function should return True if the word contains the letter and False if it does not.

def letter_check(word, letter):
    if letter in word:
        return True
    else:
        return False

example = letter_check("strawberry", "berry")
print(example)

# Write a function called contains that takes two arguments, big_string and little_string and returns True if big_string contains little_string.

def contains(big_string, little_string):
    return little_string in big_string

example = contains("Red Raiders", "Red")
print(example)

# Write a function called common_letters that takes two arguments, string_one and string_two and then returns a list with all of the letters they have in common.

def common_letters(string_one, string_two):
    common = []
    for letter in string_one:
        if (letter in string_two) and not (letter in common):
            common.append(letter)
    return common

example = common_letters("Captain", "Crunch")
print(example)