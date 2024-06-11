class TaskManager:
    def init(self):
        self.tasks = {}

    def add_task(self, task_id, description):
        if task_id in self.tasks:
            return "Task ID already exists."
        self.tasks[task_id] = description
        return "Task added."

    def get_task(self, task_id):
        return self.tasks.get(task_id, "Task not found.")

    def remove_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
            return "Task removed."
        return "Task not found."