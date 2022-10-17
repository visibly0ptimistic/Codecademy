# Write a function called poem_title_card that takes two inputs: the first input should be title and the second poet. The function should use .format() to return the given string.

def poem_title_card(title, poet):
    poem_desc = "The poem \"{}\" is written by {}.".format(title, poet)
    return poem_desc

# The function poem_description is supposed to use .format() to print out some quick information about a poem

def poem_description(publishing_date, author, title, original_work):
    poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date = publishing_date, author = author, title = title, original_work = original_work)
    return poem_desc

author = "Shel Silverstein"
title = "My Beard"
original_work = "Where the Sidewalk Ends"
publishing_date = "1974"

my_beard_description = poem_description(publishing_date, author, title, original_work)

print(my_beard_description)