# Calculate the Ticket Price based on their age
# Ticket price for users under 16 = $7.50, users older than 16 = $10.50, users older than 65 = $6.50
age = int(input("How old are you?:  "))
if age < 12:
    price = 7.50
elif age > 16:
    price = 10.50
else:
    price = 6.50
print("The price of your ticket is: " + str(price))
