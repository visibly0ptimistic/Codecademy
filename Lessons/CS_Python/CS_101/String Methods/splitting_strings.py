# Use .split() to create a list called line_one_words that contains each word in this line of poetry.
line_one = "The sky has given over"

line_one_words = line_one.split()
print(line_one_words)

# Using .split() and the provided string, create a list called author_names containing each individual author name as it’s own string.
authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(",")
print(author_names)

author_last_names = []
for name in author_names:
    author_last_names.append(name.split()[-1])
print(author_last_names)

# Create a list called spring_storm_lines that contains a string for each line of Spring Storm.
spring_storm_text = \
"""The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""

spring_storm_lines = spring_storm_text.split("\n")
print(spring_storm_lines)