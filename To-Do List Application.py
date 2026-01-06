from datetime import datetime, timedelta


#Task class

class Task:
    _id_counter = 1 

    def __init__(self, title, description="", due_date=None, priority="Medium", category="General"):
        self.task_id = f"T{Task._id_counter:03d}"
        Task._id_counter += 1

        self.title = title
        self.description = description
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d") if due_date else None
        self.priority = priority
        self.status = "Pending"
        self.creation_time = datetime.now()
        self.completion_time = None
        self.category = category

    def mark_complete(self):
        self.status = "Completed"
        self.completion_time = datetime.now()

    def update_priority(self, new_priority):
        self.priority = new_priority

    def is_overdue(self):
        if self.due_date and self.status != "Completed":
            return datetime.now() > self.due_date
        return False

    def get_task_age(self):
        return (datetime.now() - self.creation_time).days

    def extend_deadline(self, days):
        if self.due_date:
            self.due_date += timedelta(days=days)

    def __str__(self):
        due_str = self.due_date.strftime("%Y-%m-%d") if self.due_date else "N/A"
        return f"[{self.task_id}] {self.title} | Priority: {self.priority} | Status: {self.status} | Due: {due_str} | Category: {self.category}"
    
# TaskList class


class TaskList:
    def __init__(self, project_name):
        self.project_name = project_name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task added successfully! Task ID: {task.task_id}")

    def remove_task(self, task_id):
        task = self.find_task(task_id)
        if task:
            self.tasks.remove(task)
            print(f"Task {task_id} removed successfully!")
        else:
            print(f"Task {task_id} not found.")

    def find_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None

    def get_tasks_by_status(self, status):
        return [task for task in self.tasks if task.status.lower() == status.lower()]

    def get_tasks_by_priority(self, priority):
        return [task for task in self.tasks if task.priority.lower() == priority.lower()]

    def get_overdue_tasks(self):
        return [task for task in self.tasks if task.is_overdue()]

    def calculate_completion(self):
        if not self.tasks:
            return 0
        completed = len([task for task in self.tasks if task.status == "Completed"])
        return round((completed / len(self.tasks)) * 100, 2)

    def sort_tasks(self, criteria="due_date"):
        if criteria == "due_date":
            self.tasks.sort(key=lambda x: x.due_date or datetime.max)
        elif criteria == "priority":
            priority_order = {"High": 1, "Medium": 2, "Low": 3}
            self.tasks.sort(key=lambda x: priority_order.get(x.priority, 99))
        elif criteria == "creation_time":
            self.tasks.sort(key=lambda x: x.creation_time)

    def view_all_tasks(self):
        for task in self.tasks:
            print(task)


# User Flow class

def main():
    project = TaskList("My Project")

    while True:
        print("\n=== TO-DO LIST MANAGER ===")
        print("1. Add New Task")
        print("2. View All Tasks")
        print("3. View Pending Tasks")
        print("4. Mark Task Complete")
        print("5. Edit Task Priority")
        print("6. Delete Task")
        print("7. View Statistics")
        print("8. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            priority = input("Enter priority (High/Medium/Low): ")
            category = input("Enter category: ")
            task = Task(title, description, due_date, priority, category)
            project.add_task(task)

        elif choice == "2":
            project.view_all_tasks()

        elif choice == "3":
            pending_tasks = project.get_tasks_by_status("Pending")
            for task in pending_tasks:
                print(task)

        elif choice == "4":
            task_id = input("Enter task ID to mark complete: ")
            task = project.find_task(task_id)
            if task:
                task.mark_complete()
                print(f"Task {task_id} marked as complete.")
            else:
                print("Task not found.")

        elif choice == "5":
            task_id = input("Enter task ID to update priority: ")
            task = project.find_task(task_id)
            if task:
                new_priority = input("Enter new priority (High/Medium/Low): ")
                task.update_priority(new_priority)
                print("Priority updated successfully.")
            else:
                print("Task not found.")

        elif choice == "6":
            task_id = input("Enter task ID to delete: ")
            project.remove_task(task_id)

        elif choice == "7":
            print(f"Completion: {project.calculate_completion()}%")
            overdue = project.get_overdue_tasks()
            if overdue:
                print("\nOverdue Tasks:")
                for task in overdue:
                    print(task)

        elif choice == "8":
            print("Exiting To-Do List Manager...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
