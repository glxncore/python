import random

# Store prices per kilogram
rice_price = 45
sugar_price = 40
oil_price = 130

# Store quantities
rice_quantity = 3
sugar_quantity = 2.5
oil_quantity = 1.8

# Calculate total price for each item
rice_total = rice_price * rice_quantity
sugar_total = sugar_price * sugar_quantity
oil_total = oil_price * oil_quantity

# Calculate final total bill
total_bill = rice_total + sugar_total + oil_total

# Print individual item totals
print("Rice total:", rice_total)
print("Sugar total:", sugar_total)
print("Oil total:", oil_total)

# Print total bill
print("Total bill:", total_bill)

# Convert total bill to integer
total_integer = int(total_bill)
print("Total bill as integer:", total_integer)

# Convert total bill to string
total_string = str(total_bill)
print("Total bill as string:", total_string)

# Generate random delivery charge between ₹5 and ₹10
delivery_charge = random.randint(5, 10)

# Calculate final bill including delivery charge
final_bill = total_bill + delivery_charge

print("Delivery charge:", delivery_charge)
print("Final bill:", final_bill)