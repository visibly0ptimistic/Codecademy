def radix_sort(to_be_sorted):
    # finding the max_exponent the number of digits in the largest number, cast it to a string, and take the length of that string.
    maximum_value = max(to_be_sorted)
    max_exponent = len(str(maximum_value))
    sorted = to_be_sorted[:]

    # iterating through each of the exponents.
    for exponent in range(max_exponent):
        position = exponent + 1
        index = -position

        digits = [[] for i in range(10)]

        # For every iteration a version of the sorted of the previously sorted list is compared to the current list. Until the digits in the largest position of the largest number in the list are all sorted.
        for number in sorted:
            number_as_a_string = str(number)
            try:
                digit = number_as_a_string[index]
            except IndexError:
                digit = 0
            digit = int(digit)

            digits[digit].append(number)

        # create a bucket to store the list of numbers that have been sorted
        sorted = []
        for numeral in digits:
            sorted.extend(numeral)

    return sorted

# test the algorithm with an unsorted list
unsorted_list = [830, 921, 163, 373, 961, 559, 89, 199, 535, 959, 40, 641, 355, 689, 621, 183, 182, 524, 1]
print(radix_sort(unsorted_list))