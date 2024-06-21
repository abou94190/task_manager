# test unitaire

import unittest
import sys , os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.task_manager import TaskManager

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        # Initialisation de TaskManager avant chaque test
        self.manager = TaskManager()

    def test_register_user(self):
        # Test de l'inscription d'un nouvel utilisateur
        result = self.manager.register("user1", "password")
        self.assertEqual(result, "User registered.")
        self.assertIn("user1", self.manager.users)

    def test_register_existing_user(self):
        # Test de l'inscription d'un utilisateur déjà existant
        self.manager.register("user1", "password")
        result = self.manager.register("user1", "password")
        self.assertEqual(result, "Username already exists.")

    def test_login_user(self):
        # Test de la connexion d'un utilisateur avec les bonnes informations
        self.manager.register("user1", "password")
        result = self.manager.login("user1", "password")
        self.assertEqual(result, "Login successful.")
        self.assertEqual(self.manager.current_user, "user1")

    def test_login_invalid_user(self):
        # Test de la connexion avec des informations incorrectes
        result = self.manager.login("user1", "password")
        self.assertEqual(result, "Invalid username or password.")

    def test_logout_user(self):
        # Test de la déconnexion de l'utilisateur
        self.manager.register("user1", "password")
        self.manager.login("user1", "password")
        result = self.manager.logout()
        self.assertEqual(result, "Logout successful.")
        self.assertIsNone(self.manager.current_user)

    def test_update_profile(self):
        # Test de la mise à jour du profil utilisateur
        self.manager.register("user1", "password")
        self.manager.login("user1", "password")
        profile_info = {"email": "user1@example.com"}
        result = self.manager.update_profile(profile_info)
        self.assertEqual(result, "Profile updated.")
        self.assertEqual(self.manager.users["user1"]["profile"], profile_info)

    def test_add_task(self):
        # Test de l'ajout d'une nouvelle tâche
        self.manager.register("user1", "password")
        self.manager.login("user1", "password")
        result = self.manager.add_task("task1", "description1", "high")
        self.assertEqual(result, "Task added.")
        self.assertIn("task1", self.manager.users["user1"]["tasks"])

    def test_add_existing_task(self):
        # Test de l'ajout d'une tâche avec un ID déjà existant
        self.manager.register("user1", "password")
        self.manager.login("user1", "password")
        self.manager.add_task("task1", "description1")
        result = self.manager.add_task("task1", "description2")
        self.assertEqual(result, "Task ID already exists.")

    def test_get_task(self):
        # Test de la récupération d'une tâche existante
        self.manager.register("user1", "password")
        self.manager.login("user1", "password")
        self.manager.add_task("task1", "description1")
        task = self.manager.get_task("task1")
        self.assertEqual(task["description"], "description1")

    def test_get_nonexistent_task(self):
        # Test de la récupération d'une tâche inexistante
        self.manager.register("user1", "password")
        self.manager.login("user1", "password")
        result = self.manager.get_task("task1")
        self.assertEqual(result, "Task not found.")

    def test_remove_task(self):
        # Test de la suppression d'une tâche existante
        self.manager.register("user1", "password")
        self.manager.login("user1", "password")
        self.manager.add_task("task1", "description1")
        result = self.manager.remove_task("task1")
        self.assertEqual(result, "Task removed.")
        self.assertNotIn("task1", self.manager.users["user1"]["tasks"])

    def test_remove_nonexistent_task(self):
        # Test de la suppression d'une tâche inexistante
        self.manager.register("user1", "password")
        self.manager.login("user1", "password")
        result = self.manager.remove_task("task1")
        self.assertEqual(result, "Task not found.")

    def test_mark_task_completed(self):
        # Test du marquage d'une tâche comme terminée
        self.manager.register("user1", "password")
        self.manager.login("user1", "password")
        self.manager.add_task("task1", "description1")
        result = self.manager.mark_task_completed("task1")
        self.assertEqual(result, "Task marked as completed.")
        self.assertTrue(self.manager.users["user1"]["tasks"]["task1"]["completed"])

    def test_update_task(self):
        # Test de la mise à jour d'une tâche existante
        self.manager.register("user1", "password")
        self.manager.login("user1", "password")
        self.manager.add_task("task1", "description1")
        result = self.manager.update_task("task1", "new description", "high")
        self.assertEqual(result, "Task updated.")
        task = self.manager.get_task("task1")
        self.assertEqual(task["description"], "new description")
        self.assertEqual(task["priority"], "high")

    def test_get_all_tasks(self):
        # Test de la récupération de toutes les tâches d'un utilisateur
        self.manager.register("user1", "password")
        self.manager.login("user1", "password")
        self.manager.add_task("task1", "description1")
        self.manager.add_task("task2", "description2", "high")
        tasks = self.manager.get_all_tasks()
        self.assertEqual(len(tasks), 2)

    def test_get_completed_tasks(self):
        # Test de la récupération des tâches terminées
        self.manager.register("user1", "password")
        self.manager.login("user1", "password")
        self.manager.add_task("task1", "description1")
        self.manager.add_task("task2", "description2", "high")
        self.manager.mark_task_completed("task1")
        completed_tasks = self.manager.get_all_tasks(filter_by="completed")
        self.assertEqual(len(completed_tasks), 1)
        self.assertIn("task1", completed_tasks)

    def test_get_pending_tasks(self):
        # Test de la récupération des tâches en attente
        self.manager.register("user1", "password")
        self.manager.login("user1", "password")
        self.manager.add_task("task1", "description1")
        self.manager.add_task("task2", "description2", "high")
        self.manager.mark_task_completed("task1")
        pending_tasks = self.manager.get_all_tasks(filter_by="pending")
        self.assertEqual(len(pending_tasks), 1)
        self.assertIn("task2", pending_tasks)

    def test_get_priority_sorted_tasks(self):
        # Test de la récupération des tâches triées par priorité
        self.manager.register("user1", "password")
        self.manager.login("user1", "password")
        self.manager.add_task("task1", "description1", "low")
        self.manager.add_task("task2", "description2", "high")
        priority_sorted_tasks = self.manager.get_all_tasks(filter_by="priority")
        self.assertEqual(list(priority_sorted_tasks.keys()), ["task2", "task1"])
