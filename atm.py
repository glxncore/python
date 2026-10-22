class ATM:
    def __init__(self, name):
        self._name = name
        self._balance = 0
        self._history = []

    def check_balance(self):
        print("Current Balance: Rs.", self._balance)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self._history.append(f"Deposited: Rs. {amount}")
            print("Deposit successful!")
        else:
            print("Invalid amount!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount!")
        elif amount > self._balance:
            print("Insufficient balance!")
        else:
            self._balance -= amount
            self._history.append(f"Withdrawn: Rs. {amount}")
            print("Withdrawal successful!")

    def transaction_history(self):
        if not self._history:
            print("No transactions yet.")
        else:
            print("\nTransaction History:")
            for transaction in self._history:
                print(transaction)

    def display_details(self):
        print("\nAccount Holder:", self._name)
        print("Balance: Rs.", self._balance)


# Main program
name = input("Enter account holder name: ")
atm = ATM(name)

while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transaction History")
    print("5. Account Details")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        atm.check_balance()

    elif choice == "2":
        amount = float(input("Enter deposit amount: Rs. "))
        atm.deposit(amount)

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: Rs. "))
        atm.withdraw(amount)

    elif choice == "4":
        atm.transaction_history()

    elif choice == "5":
        atm.display_details()

    elif choice == "6":
        print("Thank you for using our ATM!")
        break

    else:
        print("Invalid choice! Please try again.")