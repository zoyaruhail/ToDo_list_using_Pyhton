def todolist():
    try:
        name = input("Enter your name: ").strip()
        filename = f"{name}.txt"

        # Create file only if it does not exist
        try:
            with open(filename, 'x') as file:
                file.write(f"Hello! {name}, Welcome To Your ToDo List\n")
                print("File created successfully!")
        except FileExistsError:
            print("Welcome back! Your To-Do List is ready.")

        while True:
            menu = int(input("\n|| Menu || \n1. Add Task \n2. Remove Task \n3. View Task \n4. Exit \nChoose your option: "))

            if menu == 1:  # Add Task
                task = input("Enter Task: ").strip()
                if task:
                    with open(filename, 'a') as file:
                        file.write(task + "\n")  # Ensures each task is on a new line
                    print("Task added successfully!")
                else:
                    print("Empty task cannot be entered.")

            elif menu == 2:  # Remove Task
                try:
                    with open(filename, 'r') as file:
                        task_list = file.readlines()

                    if len(task_list) <= 1:  # Check if tasks exist (excluding welcome line)
                        print("No tasks to remove.")
                        continue

                    print("\nYour To-Do List:")
                    for i, task in enumerate(task_list[1:], 1):  # Skipping first line (welcome message)
                        print(f"{i}. {task.strip()}")

                    num = int(input("Enter the task number to remove: "))   
                    if 1 <= num < len(task_list):
                        removed_task = task_list.pop(num)  # Remove the selected task
                        with open(filename, 'w') as file:
                            file.writelines(task_list)  # Save updated task list
                        print(f"Task '{removed_task.strip()}' removed successfully!")
                    else:
                        print("Invalid task number!")
                except FileNotFoundError:
                    print("File does not exist.")

            elif menu == 3:  # View Task
                try:
                    with open(filename, 'r') as file:
                        task_list = file.readlines()

                    if len(task_list) <= 1:  # No tasks present
                        print("No tasks found.")
                    else:
                        print(f"\n{name}'s To-Do List:")
                        for i, task in enumerate(task_list[1:], 1):
                            print(f"{i}. {task.strip()}")
                except FileNotFoundError:
                    print("File does not exist.")

            elif menu == 4:  # Exit
                print(f"Thank You {name}, Your To-Do List is saved.")
                break

            else:
                print("Invalid input! Please choose a valid option.")

    except ValueError:
        print("Invalid input! Please enter a number.")

todolist()
