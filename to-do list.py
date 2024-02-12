tasks = []

while True:
    print("\n1. Show Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        if not tasks:
            print("No tasks found.")
        else:
            print("Your To-Do List:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
    elif choice == '2':
        new_task = input("Enter the task: ")
        tasks.append(new_task)
        print(f"Task '{new_task}' added successfully.")
    elif choice == '3':
        if not tasks:
            print("No tasks to remove.")
        else:
            print("Your To-Do List:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
            task_index = int(input("Enter the task index to remove: "))
            if 1 <= task_index <= len(tasks):
                removed_task = tasks.pop(task_index - 1)
                print(f"Task '{removed_task}' removed successfully.")
            else:
                print("Invalid task index.")
    elif choice == '4':
        print("Quitting the To-Do List application. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")