# Calculate data from carly's clippers
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#sum up all the prices of haircuts.
total_price = 0

for price in prices:
    total_price += price
print(total_price)

# find the average price
average_price = total_price / len(prices)
print("Average Haircut Price: " + str(average_price))

# decrease all prices by 5 dollars
new_prices = [price - 5 for price in prices]
print(new_prices)

# calculate last week's revenue
total_revenue = 0
for i in range(0, len(hairstyles)):
    total_revenue += prices[i] * last_week[i]
print("Total Revenue: " + str(total_revenue))

# find the average daily revenue
average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

# advertise all haircuts under 30 dollars
cuts_under_30 = [price for price in new_prices if price < 30]
print(cuts_under_30)