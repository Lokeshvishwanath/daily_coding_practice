# Day 23 - To-Do List Application

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return

        print("\n=== Your Tasks ===")

        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")

    def remove_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            removed = self.tasks.pop(task_number - 1)
            print(f"Task '{removed}' removed successfully!")
        else:
            print("Invalid task number.")


def main():
    todo = TodoList()

    while True:
        print("\n==== TO-DO LIST MENU ====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            todo.add_task(task)

        elif choice == "2":
            todo.view_tasks()

        elif choice == "3":
            todo.view_tasks()
            number = int(input("Enter task number to remove: "))
            todo.remove_task(number)

        elif choice == "4":
            print("Exiting application...")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()