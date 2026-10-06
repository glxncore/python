import random

# Store the volume of each juice
apple = 15.5
orange = 20
grape = 10.25

# Calculate total volume
total = apple + orange + grape

# Print total volume
print("Total volume:", total, "liters")

# Convert total volume to integer
print("Integer volume:", int(total))

# Convert total volume to string
total_string = str(total)
print("The total volume as a string is:", total_string)

# Add a random bonus between 5 and 10 liters
bonus = random.randint(5, 10)
final_total = total + bonus

print("Bonus liters:", bonus)
print("Final total:", final_total, "liters")