#In this project, I will store the names and prices of a furniture store’s catalog in variables. 
# Then I will process the total price and item list of customers by printing them to the output terminal.

lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."

lovely_loveseat_price = 254.00

stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."

stylish_settee_price = 180.50

luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."

luxurious_lamp_price = 52.12

# A sales tax of 8.8% is applied to all purchases
sales_tax = .088

# CUSTOMER 1
customer_one_total = 0
customer_one_itemization = " "

# c1 itemization
customer_one_itemization = luxurious_lamp_description + "\n" + lovely_loveseat_description

# c1 total
customer_one_total += lovely_loveseat_price
customer_one_total += luxurious_lamp_price

# CUSTOMER 1 is ready to check out
# Calculate Sales Tax
customer_one_tax = customer_one_total * sales_tax
# Apply Sales Tax
customer_one_tax += customer_one_total

# Print CUSTOMER 1 Receipt
print("Customer One Items:")
print(customer_one_itemization)

print("Customer One Total:")
print(customer_one_total)