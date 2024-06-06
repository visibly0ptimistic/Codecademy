weight = 1.5
price_per_pound = 1
flat_charge = 20

#Ground Shipping
# if / elif / else checks weight and prints cost

if weight <= 2:
    price_per_pound = 1.5
elif weight <= 6:
    price_per_pound = 3
elif weight <= 10:
    price_per_pound = 4
elif weight < 10:
    price_per_pound = 4.75

cost_ground = ((weight * price_per_pound) + flat_charge)

print(f"Ground Shipping: ${cost_ground}") 

#Ground Shipping Premium
#Flat charge: $125.00

cost_ground_premium = flat_charge * 6.25

print(f"Ground Shipping Premium: ${cost_ground_premium}") 

#Drone Shipping
# if / elif / else checks weight and prints cost

if weight <= 2:
    price_per_pound = 4.5
elif weight <= 6:
    price_per_pound = 9
elif weight <= 10:
    price_per_pound = 12
elif weight < 10:
    price_per_pound = 14.25

cost_drone = (weight * price_per_pound)

print(f"Drone Shipping: ${cost_drone}")