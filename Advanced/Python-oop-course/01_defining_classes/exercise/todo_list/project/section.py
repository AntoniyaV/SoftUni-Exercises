class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"
        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        completed_tasks = [task for task in self.tasks if task.completed]
        for task in completed_tasks:
            self.tasks.remove(task)
        return f"Cleared {len(completed_tasks)} tasks."

    def view_section(self):
        info = f"Section {self.name}:\n"
        info += '\n'.join([task.details() for task in self.tasks])
        return info
