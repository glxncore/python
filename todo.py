todos = []

while True:
    print("\n1. Add task")
    print("2. Show today's tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        time = input("Enter time (HH:MM AM/PM): ")
        todos.append((time, task))
        print("Task added successfully!")

    elif choice == "2":
        print("\nToday's To-Do List:")

        if not todos:
            print("No tasks added yet.")
        else:
            for time, task in todos:
                print(f"{time} - {task}")

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")