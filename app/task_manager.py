class TaskManager:
    def __init__(self):
        # Initialise un dictionnaire pour stocker les utilisateurs et un attribut pour l'utilisateur actuellement connecté
        self.users = {}
        self.current_user = None

    def register(self, username, password):
        # Vérifie si le nom d'utilisateur existe déjà
        if username in self.users:
            return "Username already exists."
        # Enregistre un nouvel utilisateur avec son mot de passe et initialise ses tâches et profil
        self.users[username] = {
            "password": password,
            "tasks": {},
            "profile": {}
        }
        return "User registered."

    def login(self, username, password):
        # Récupère l'utilisateur et vérifie le mot de passe
        user = self.users.get(username)
        if user and user["password"] == password:
            self.current_user = username
            return "Login successful."
        return "Invalid username or password."

    def logout(self):
        # Déconnecte l'utilisateur actuel
        self.current_user = None
        return "Logout successful."

    def update_profile(self, profile_info):
        # Vérifie qu'un utilisateur est connecté, puis met à jour son profil
        if not self.current_user:
            return "No user logged in."
        self.users[self.current_user]["profile"] = profile_info
        return "Profile updated."

    def add_task(self, task_id, description, priority="normal"):
        # Vérifie qu'un utilisateur est connecté, puis ajoute une tâche si l'ID de la tâche n'existe pas déjà
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
        # Vérifie qu'un utilisateur est connecté, puis retourne la tâche correspondante si elle existe
        if not self.current_user:
            return "No user logged in."
        task = self.users[self.current_user]["tasks"].get(task_id)
        return task if task else "Task not found."

    def remove_task(self, task_id):
        # Vérifie qu'un utilisateur est connecté, puis supprime la tâche correspondante si elle existe
        if not self.current_user:
            return "No user logged in."
        tasks = self.users[self.current_user]["tasks"]
        if task_id in tasks:
            del tasks[task_id]
            return "Task removed."
        return "Task not found."

    def mark_task_completed(self, task_id):
        # Vérifie qu'un utilisateur est connecté, puis marque la tâche comme complétée si elle existe
        if not self.current_user:
            return "No user logged in."
        tasks = self.users[self.current_user]["tasks"]
        if task_id in tasks:
            tasks[task_id]["completed"] = True
            return "Task marked as completed."
        return "Task not found."

    def update_task(self, task_id, description=None, priority=None):
        # Vérifie qu'un utilisateur est connecté, puis met à jour la description et/ou la priorité de la tâche si elle existe
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
        # Vérifie qu'un utilisateur est connecté, puis retourne toutes les tâches selon le filtre spécifié (toutes, complétées, en attente, par priorité)
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

