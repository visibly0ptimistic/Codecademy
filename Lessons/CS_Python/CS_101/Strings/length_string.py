first_name = "Reiko"
last_name = "Matsuki"

# Write a function called password_generator() that takes two inputs, first_name and last_name, and then concatenates the last three letters of each and returns them as a string.

def password_generator(first_name, last_name):
    password = first_name[len(first_name)-3:] + last_name[len(last_name)-3:]
    return password

temp_password = password_generator(first_name, last_name)

print(temp_password)
