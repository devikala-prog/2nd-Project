import json


TODO_FILE = 'todo_list.json'


def load_tasks():
    try:
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_tasks(tasks):
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file)


def display_tasks(tasks):
    if not tasks:
        print("No tasks in the todo list.")
    else:
        print("Todo List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")


def todo_list():
    tasks = load_tasks()

    while True:
        print("\nTodo List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            task = input("Enter the task: ")
            tasks.append(task)
            save_tasks(tasks)
            print("Task added successfully.")

        elif choice == '2':
            display_tasks(tasks)

        elif choice == '3':
            display_tasks(tasks)
            try:
                task_num = int(input("Enter the task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    deleted_task = tasks.pop(task_num - 1)
                    save_tasks(tasks)
                    print(f"Deleted task: {deleted_task}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '4':
            print("Exiting the Todo List application.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    todo_list()
