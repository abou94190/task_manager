import unittest
from app.task_manager import TaskManager


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.tm = TaskManager()

    def test_register_user(self):
        response = self.tm.register("user1", "password1")
        self.assertEqual(response, "User registered.")
        self.assertIn("user1", self.tm.users)

    def test_register_existing_user(self):
        self.tm.register("user1", "password1")
        response = self.tm.register("user1", "password1")
        self.assertEqual(response, "Username already exists.")

    def test_login_user(self):
        self.tm.register("user1", "password1")
        response = self.tm.login("user1", "password1")
        self.assertEqual(response, "Login successful.")
        self.assertEqual(self.tm.current_user, "user1")

    def test_login_invalid_user(self):
        response = self.tm.login("user1", "password1")
        self.assertEqual(response, "Invalid username or password.")
        self.assertIsNone(self.tm.current_user)

    def test_logout_user(self):
        self.tm.register("user1", "password1")
        self.tm.login("user1", "password1")
        response = self.tm.logout()
        self.assertEqual(response, "Logout successful.")
        self.assertIsNone(self.tm.current_user)

    def test_update_profile(self):
        self.tm.register("user1", "password1")
        self.tm.login("user1", "password1")
        profile_info = {"email": "user1@example.com"}
        response = self.tm.update_profile(profile_info)
        self.assertEqual(response, "Profile updated.")
        self.assertEqual(self.tm.users["user1"]["profile"], profile_info)

    def test_add_task(self):
        self.tm.register("user1", "password1")
        self.tm.login("user1", "password1")
        response = self.tm.add_task("task1", "description1")
        self.assertEqual(response, "Task added.")
        self.assertIn("task1", self.tm.users["user1"]["tasks"])

    def test_add_existing_task(self):
        self.tm.register("user1", "password1")
        self.tm.login("user1", "password1")
        self.tm.add_task("task1", "description1")
        response = self.tm.add_task("task1", "description1")
        self.assertEqual(response, "Task ID already exists.")

    def test_get_task(self):
        self.tm.register("user1", "password1")
        self.tm.login("user1", "password1")
        self.tm.add_task("task1", "description1")
        task = self.tm.get_task("task1")
        self.assertIsNotNone(task)
        self.assertEqual(task["description"], "description1")

    def test_get_nonexistent_task(self):
        self.tm.register("user1", "password1")
        self.tm.login("user1", "password1")
        task = self.tm.get_task("task1")
        self.assertEqual(task, "Task not found.")

    def test_remove_task(self):
        self.tm.register("user1", "password1")
        self.tm.login("user1", "password1")
        self.tm.add_task("task1", "description1")
        response = self.tm.remove_task("task1")
        self.assertEqual(response, "Task removed.")
        self.assertNotIn("task1", self.tm.users["user1"]["tasks"])

    def test_mark_task_completed(self):
        self.tm.register("user1", "password1")
        self.tm.login("user1", "password1")
        self.tm.add_task("task1", "description1")
        response = self.tm.mark_task_completed("task1")
        self.assertEqual(response, "Task marked as completed.")
        self.assertTrue(self.tm.users["user1"]["tasks"]["task1"]["completed"])

    def test_update_task(self):
        self.tm.register("user1", "password1")
        self.tm.login("user1", "password1")
        self.tm.add_task("task1", "description1")
        response = self.tm.update_task("task1", description="new description", priority="high")
        self.assertEqual(response, "Task updated.")
        self.assertEqual(self.tm.users["user1"]["tasks"]["task1"]["description"], "new description")
        self.assertEqual(self.tm.users["user1"]["tasks"]["task1"]["priority"], "high")

    def test_get_all_tasks(self):
        self.tm.register("user1", "password1")
        self.tm.login("user1", "password1")
        self.tm.add_task("task1", "description1", priority="high")
        self.tm.add_task("task2", "description2", priority="low")
        all_tasks = self.tm.get_all_tasks()
        self.assertEqual(len(all_tasks), 2)
        completed_tasks = self.tm.get_all_tasks(filter_by="completed")
        self.assertEqual(len(completed_tasks), 0)
        self.tm.mark_task_completed("task1")
        completed_tasks = self.tm.get_all_tasks(filter_by="completed")
        self.assertEqual(len(completed_tasks), 1)


if __name__ == '__main__':
    unittest.main()
