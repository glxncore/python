# Receipt header using a multiline string
header = """\tBOOKSTORE RECEIPT
----------------------------
"""

# Book details
book1 = "Python Basics"
price1 = 450

book2 = "Data Science Intro"
price2 = 600

# Create each book line using {} placeholders and format()
line1 = "\t{} \t₹{}".format(book1, price1)
line2 = "\t{} \t₹{}".format(book2, price2)

# Calculate total
total = price1 + price2
total_line = "\tTOTAL \t₹{}".format(total)

# Thank-you message
thank_you = "\n\tTHANK YOU FOR SHOPPING WITH US!"

# Concatenate the complete receipt
receipt = header + line1 + "\n" + line2 + "\n" + total_line + thank_you

# Display the entire receipt in uppercase
print(receipt.upper())