# use randrange to produce a random index
from random import randrange

def quicksort(list, start, end):
    if start >= end:
        return list
# Define your pivot variables below

# Swap the elements in list below

# Leave these lines for testing
    print(list[start])
    start += 1
    return quicksort(list, start, end)


my_list = [32, 22]
print("BEFORE: ", my_list)
sorted_list = quicksort(my_list, 0, len(my_list) - 1)
print("AFTER: ", sorted_list)