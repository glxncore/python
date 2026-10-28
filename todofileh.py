while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")

        with open("tasks.txt", "a") as file:
            file.write(task + "\n")

        print("Task added successfully!")

    elif choice == "2":
        try:
            with open("tasks.txt", "r") as file:
                tasks = file.readlines()

            if not tasks:
                print("No tasks found.")
            else:
                for i, task in enumerate(tasks, 1):
                    print(i, task.strip())

        except FileNotFoundError:
            print("No tasks found.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")