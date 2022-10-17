first_name = "Julie"
last_name = "Blevins"

# concatenate the first three letters of each and then return the new account name.

def account_generator(first_name, last_name):
    new_account_name = first_name[:3] + last_name[:3]
    return new_account_name

new_account = account_generator(first_name, last_name)
print(new_account)