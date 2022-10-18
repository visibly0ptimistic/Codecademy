def square_list_in_place(int_list):
    for index, element in enumerate(int_list):
        int_list[index] *= element

    # NOTE: no need to return anything - we modified
    # int_list in place


def square_list_out_of_place(int_list):
    # We allocate a new list with the length of the input list
    squared_list = [None] * len(int_list)

    for index, element in enumerate(int_list):
        squared_list[index] = element ** 2

    return squared_list

original_list = [2, 3, 4, 5]
square_list_in_place(original_list)

print("original list: %s" % original_list)
# Prints: original list: [4, 9, 16, 25], confusingly!