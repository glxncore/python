try:
    title = input("Enter book title: ")
    year = input("Enter publication year: ")

    if not title.replace(" ", "").isalpha():
        raise ValueError("Book title must contain only alphabets and spaces.")

    if not (len(year) == 4 and year.isdigit() and year.startswith(("19", "20"))):
        raise ValueError("Publication year must be a 4-digit number starting with 19 or 20.")

    print("Book title:", title)
    print("Publication year:", year)
    print("Book details accepted successfully.")

except ValueError as e:
    print("Error:", e)

finally:
    print("Library system execution completed.")