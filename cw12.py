import re

try:
    title = input("Enter book title: ")
    year = input("Enter publication year: ")

    if not re.fullmatch(r"[A-Za-z ]+", title):
        raise ValueError("Book title must contain only alphabets and spaces.")

    if not re.fullmatch(r"(19|20)[0-9]{2}", year):
        raise ValueError("Publication year must be a 4-digit number starting with 19 or 20.")

    print("Book details accepted successfully!")

except ValueError as e:
    print("Error:", e)

finally:
    print("Library system execution completed.")