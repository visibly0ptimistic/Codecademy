def radix_sort(to_be_sorted):
    maximum_value = max(to_be_sorted)
    max_exponent = len(str(maximum_value))

    # create copy of to_be_sorted here
    being_sorted = to_be_sorted[:]
    digits = [[] for digit in range(10)]
    return digits