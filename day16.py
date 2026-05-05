import random
import datetime

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "created_at": datetime.datetime.now(),
            "completed": False
        }
        self.tasks.append(task)

    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                return True
        return False

    def get_pending_tasks(self):
        return [task for task in self.tasks if not task["completed"]]

    def save_to_file(self, filename="tasks.txt"):
        with open(filename, "w") as f:
            for task in self.tasks:
                f.write(f"{task['id']} | {task['title']} | {task['completed']}\n")


def generate_random_tasks(manager, count=5):
    sample_tasks = [
        "Learn Python",
        "Build MERN project",
        "Read a book",
        "Workout",
        "Practice DSA",
        "Write blog",
        "Revise concepts"
    ]
    for _ in range(count):
        manager.add_task(random.choice(sample_tasks))


def main():
    manager = TaskManager()
    generate_random_tasks(manager, 7)

    print("All Tasks:")
    for task in manager.tasks:
        print(task)

    # Randomly complete a task
    random_id = random.randint(1, len(manager.tasks))
    manager.complete_task(random_id)

    print("\nPending Tasks:")
    for task in manager.get_pending_tasks():
        print(task)

    manager.save_to_file()


if __name__ == "__main__":
    main()