class TaskManager:
    def __init__(self):
        self.users = {}
        self.current_user = None

    def register(self, username, password):
        if username in self.users:
            return "Username already exists."
        self.users[username] = {
            "password": password,
            "tasks": {},
            "profile": {}
        }
        return "User registered."

    def login(self, username, password):
        user = self.users.get(username)
        if user and user["password"] == password:
            self.current_user = username
            return "Login successful."
        return "Invalid username or password."

    def logout(self):
        self.current_user = None
        return "Logout successful."

    def update_profile(self, profile_info):
        if not self.current_user:
            return "No user logged in."
        self.users[self.current_user]["profile"] = profile_info
        return "Profile updated."

    def add_task(self, task_id, description, priority="normal"):
        if not self.current_user:
            return "No user logged in."
        tasks = self.users[self.current_user]["tasks"]
        if task_id in tasks:
            return "Task ID already exists."
        tasks[task_id] = {
            "description": description,
            "priority": priority,
            "completed": False
        }
        return "Task added."

    def get_task(self, task_id):
        if not self.current_user:
            return "No user logged in."
        task = self.users[self.current_user]["tasks"].get(task_id)
        return task if task else "Task not found."

    def remove_task(self, task_id):
        if not self.current_user:
            return "No user logged in."
        tasks = self.users[self.current_user]["tasks"]
        if task_id in tasks:
            del tasks[task_id]
            return "Task removed."
        return "Task not found."

    def mark_task_completed(self, task_id):
        if not self.current_user:
            return "No user logged in."
        tasks = self.users[self.current_user]["tasks"]
        if task_id in tasks:
            tasks[task_id]["completed"] = True
            return "Task marked as completed."
        return "Task not found."

    def update_task(self, task_id, description=None, priority=None):
        if not self.current_user:
            return "No user logged in."
        tasks = self.users[self.current_user]["tasks"]
        if task_id in tasks:
            if description:
                tasks[task_id]["description"] = description
            if priority:
                tasks[task_id]["priority"] = priority
            return "Task updated."
        return "Task not found."

    def get_all_tasks(self, filter_by="all"):
        if not self.current_user:
            return "No user logged in."
        tasks = self.users[self.current_user]["tasks"]
        if filter_by == "completed":
            return {k: v for k, v in tasks.items() if v["completed"]}
        elif filter_by == "pending":
            return {k: v for k, v in tasks.items() if not v["completed"]}
        elif filter_by == "priority":
            return {k: v for k, v in sorted(tasks.items(), key=lambda item: item[1]["priority"])}
        return tasks

