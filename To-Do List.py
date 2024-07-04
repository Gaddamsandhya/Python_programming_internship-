class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.description}"
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        self.tasks.append(Task(description))

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
        else:
            print("Invalid task number.")

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
        else:
            print("Invalid task number.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")
def main():
    todo_list = ToDoList()
    while True:
        print("\nTo-Do List:")
        todo_list.list_tasks()
        print("\nOptions:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task as Completed")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == "2":
            try:
                index = int(input("Enter task number to delete: ")) - 1
                todo_list.delete_task(index)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "3":
            try:
                index = int(input("Enter task number to mark as completed: ")) - 1
                todo_list.mark_task_completed(index)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()