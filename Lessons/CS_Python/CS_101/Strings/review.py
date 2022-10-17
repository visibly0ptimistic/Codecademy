# Create a function called username_generator take two inputs, first_name and last_name and returns a username.
def username_generator(first_name, last_name):
    if len(first_name) < 3:
        username = first_name
    else:
        username = first_name[:3]
    if len(last_name) < 4:
        username += last_name
    else:
        username += last_name[:4]
    return username

# for the temporary password, take the input user name and shift all of the letters by one to the right, so the last letter of the username ends up as the first letter and so forth.
def password_generator(user_name):
    password = ""
    for i in range(0, len(user_name)):
        password += user_name[i-1]
    return password
example = password_generator("victor")
print(example)