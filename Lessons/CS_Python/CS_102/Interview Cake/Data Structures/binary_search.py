# Sorted list of items
items = [2, 4, 6, 8, 10, 12, 14]

# Defining a function called bin search with 2 parameters that we can call later with arguments of our choice
def bin_search(list, x):
    # l is the start of the list
    l = 0
    # r is the end of the list
    r = len(list)
    # while l does not equal r
    while l != r:
        # find the midpoint l+r // 2
        m = (l + r) // 2
        # if, the parameter defined as x equals the midpoint of your list
        if x == list[m]:
            # then, you have the key or index to your answer.
            return m
        # if, the parameter defined as x is less than the midpoint of your list
        if x < list[m]:
            # then, the end of the list now equals the midpoint of your list.
            r = m
        # if, the parameter defined as x is greater than the midpoint of your list.
        else:
            # then, the start of the list now equals the midpoint of the list plus 1.
            l = m + 1
    # if the parameter defined as x does not exist in your list, return None.
    return None 

# Here we call the bin search function we defined earlier. The first argument is a list and the second argument is a value in that list.
print(bin_search(items, 2))
print(bin_search(items, 8))
print(bin_search(items, 14))
print(bin_search(items, 21))  # None