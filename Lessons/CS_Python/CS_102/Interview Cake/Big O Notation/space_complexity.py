# This function takes O(1) space (we use a fixed number of variables)

def say_hi_n_times(n):
    for time in range(n):
        print("hi")

# This function takes O(n) space (the size of hi_list scales with the size of the input)

def list_of_hi_n_times(n):
    hi_list = []
    for time in range(n):
        hi_list.append("hi")
    return hi_list

# Usually when we talk about space complexity, we're talking about additional space, so we don't include space taken up by the inputs. For example, this function takes constant space even though the input has nn items:

def get_largest_item(items):
    largest = float('-inf')
    for item in items:
        if item > largest:
            largest = item
    return largest