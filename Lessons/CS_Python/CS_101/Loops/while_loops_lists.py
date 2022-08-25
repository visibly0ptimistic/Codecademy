# Using while loops for lists in python
days_of_the_week = ['Monday - ', 'Tuesday - ', 'Wednesday - ', 'Thursday - ', 'Friday - ']

python_topics = ["variables", "control flow", "loops", "modules", "classes"]

# number of iterations needed for the while loop. 5, since there are 5 topics.
five_topics = len(python_topics)

# this variable will provide a stopping condition
index = 0

# write a while loop that prints a statement for each element
#  a loop has 3 components:
#   1. a condition
#   2. a command
#   3. an increment
while index < five_topics:
    print(days_of_the_week[index] + python_topics[index])
    index += 1




