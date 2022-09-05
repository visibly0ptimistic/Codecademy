import string


tshirt_price = 9.75
shorts_price = 15.50
mug_price = 5.99
poster_price = 2.00

# The max() built-in function takes in a series of consecutive arguments and returns the max value.
max_price = max(9.75, 15.50, 5.99, 2.00)
print(max_price)

# The min() built-in function takes in a series of consecutive arguments and returns the min value.
min_price = min(9.75, 15.50, 5.99, 2.00)
print(min_price)

#The round() built-in function takes in two arguments. The first argument is the number we want to round, followed by an argument on how many decimal places we want to round it.
rounded_price = round(tshirt_price, 1)
print(rounded_price)

help(string)