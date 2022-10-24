# Define pattern_search
def pattern_search(text, pattern):
    print("Input Text:", text, "Input Pattern:", pattern)
    for index in range(len(text)):
        print("Text Index:", index)
        for char in range(len(pattern)):
            print("Pattern Index:", char)


text = "HAYHAYNEEDLEHAYHAYHAYNEEDLEHAYHAYHAYHAYNEEDLE"
pattern = "NEEDLE"
# Invoke pattern_search
pattern_search(text, pattern)