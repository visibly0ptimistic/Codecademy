# Organize customer data for Maria's web store
first_names = ["Ainsley", "Ben", "Chani", "Depak"]

preferred_size = ["Small", "Large", "Medium"]
preferred_size.append("Medium")
print(preferred_size)

# Restructure the two lists into a two-dimensional list
# a boolean value reflecting expedited shipping is added third.
customer_data = [["Ainsley", "Small", True], ["Ben", "Large", False], ["Chani", "Medium", True], ["Depak", "Medium", False]]
print(customer_data)

customer_data[2][-1] = False
customer_data[1].remove(False)

new_customers = [["Amit", "Large", True], ["Karim", "X-Large", False]]

customer_data_final = customer_data + new_customers
print(customer_data_final)
