# concatenate the string "R" with a slice of first_name that includes everything but the first character, "B", and save it to a new string fixed_first_name.

first_name = "Bob"
last_name = "Daily"

fixed_first_name = "R" + first_name[-2:]
print(fixed_first_name)
