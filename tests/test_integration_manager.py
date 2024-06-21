from app.task_manager import TaskManager
import unittest
import sys
import os

# Ajouter le répertoire racine au PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.tm = TaskManager()

    def test_user_registration_and_login(self):
        self.assertEqual(
            self.tm.register(
                "alice",
                "password123"),
            "User registered.")
        self.assertEqual(
            self.tm.register(
                "bob",
                "securepass"),
            "User registered.")
        self.assertEqual(
            self.tm.register(
                "alice",
                "newpassword"),
            "Username already exists.")

        self.assertEqual(
            self.tm.login(
                "alice",
                "wrongpassword"),
            "Invalid username or password.")
        self.assertEqual(
            self.tm.login(
                "alice",
                "password123"),
            "Login successful.")
        self.assertEqual(self.tm.logout(), "Logout successful.")
        self.assertEqual(
            self.tm.login(
                "bob",
                "securepass"),
            "Login successful.")

    def test_update_profile(self):
        self.tm.register("bob", "securepass")
        self.tm.login("bob", "securepass")
        self.assertEqual(self.tm.update_profile(
            {"email": "bob@example.com", "age": 30}), "Profile updated.")
        self.assertEqual(
            self.tm.users["bob"]["profile"], {
                "email": "bob@example.com", "age": 30})

    def test_add_task(self):
        self.tm.register("bob", "securepass")
        self.tm.login("bob", "securepass")
        self.assertEqual(
            self.tm.add_task(
                1,
                "Write unit tests",
                "high"),
            "Task added.")
        self.assertEqual(
            self.tm.add_task(
                2,
                "Fix bugs",
                "normal"),
            "Task added.")
        self.assertEqual(
            self.tm.add_task(
                1,
                "Update documentation",
                "low"),
            "Task ID already exists.")

    def test_get_task(self):
        self.tm.register("bob", "securepass")
        self.tm.login("bob", "securepass")
        self.tm.add_task(1, "Write unit tests", "high")
        self.assertEqual(self.tm.get_task(1), {
            "description": "Write unit tests",
            "priority": "high",
            "completed": False
        })
        self.assertEqual(self.tm.get_task(3), "Task not found.")

    def test_remove_task(self):
        self.tm.register("bob", "securepass")
        self.tm.login("bob", "securepass")
        self.tm.add_task(2, "Fix bugs", "normal")
        self.assertEqual(self.tm.remove_task(2), "Task removed.")
        self.assertEqual(self.tm.remove_task(2), "Task not found.")

    def test_mark_task_completed(self):
        self.tm.register("bob", "securepass")
        self.tm.login("bob", "securepass")
        self.tm.add_task(1, "Write unit tests", "high")
        self.assertEqual(
            self.tm.mark_task_completed(1),
            "Task marked as completed.")
        self.assertEqual(self.tm.mark_task_completed(3), "Task not found.")

    def test_update_task(self):
        self.tm.register("bob", "securepass")
        self.tm.login("bob", "securepass")
        self.tm.add_task(1, "Write unit tests", "high")
        self.assertEqual(
            self.tm.update_task(
                1,
                description="Write integration tests",
                priority="medium"),
            "Task updated.")
        self.assertEqual(self.tm.get_task(1), {
            "description": "Write integration tests",
            "priority": "medium",
            "completed": False
        })
        self.assertEqual(
            self.tm.update_task(
                3,
                description="New task"),
            "Task not found.")

    def test_get_all_tasks(self):
        self.tm.register("bob", "securepass")
        self.tm.login("bob", "securepass")
        self.tm.add_task(1, "Write integration tests", "medium")
        self.tm.add_task(2, "Fix bugs", "normal")
        self.tm.add_task(3, "Update documentation", "low")
        self.tm.mark_task_completed(1)

        self.assertEqual(self.tm.get_all_tasks(), {
            1: {
                "description": "Write integration tests",
                "priority": "medium",
                "completed": True
            },
            2: {
                "description": "Fix bugs",
                "priority": "normal",
                "completed": False
            },
            3: {
                "description": "Update documentation",
                "priority": "low",
                "completed": False
            }
        })
        self.assertEqual(self.tm.get_all_tasks(filter_by="completed"), {
            1: {
                "description": "Write integration tests",
                "priority": "medium",
                "completed": True
            }
        })
        self.assertEqual(self.tm.get_all_tasks(filter_by="pending"), {
            2: {
                "description": "Fix bugs",
                "priority": "normal",
                "completed": False
            },
            3: {
                "description": "Update documentation",
                "priority": "low",
                "completed": False
            }
        })
        self.assertEqual(self.tm.get_all_tasks(filter_by="priority"), {
            3: {
                "description": "Update documentation",
                "priority": "low",
                "completed": False
            },
            2: {
                "description": "Fix bugs",
                "priority": "normal",
                "completed": False
            },
            1: {
                "description": "Write integration tests",
                "priority": "medium",
                "completed": True
            }
        })


if __name__ == "__main__":
    unittest.main()
