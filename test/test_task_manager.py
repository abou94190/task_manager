import unittest

class TaskManager:
    def __init__(self):
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

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.task_manager = TaskManager()

    def test_add_task(self):
        result = self.task_manager.add_task(1, "Write code")
        self.assertEqual(result, "Task added.")
        self.assertEqual(self.task_manager.get_task(1), "Write code")

    def test_add_task_with_existing_id(self):
        self.task_manager.add_task(1, "Write code")
        result = self.task_manager.add_task(1, "Write tests")
        self.assertEqual(result, "Task ID already exists.")
        self.assertEqual(self.task_manager.get_task(1), "Write code")

    def test_get_task(self):
        self.task_manager.add_task(1, "Write code")
        result = self.task_manager.get_task(1)
        self.assertEqual(result, "Write code")

    def test_get_nonexistent_task(self):
        result = self.task_manager.get_task(2)
        self.assertEqual(result, "Task not found.")

    def test_remove_task(self):
        self.task_manager.add_task(1, "Write code")
        result = self.task_manager.remove_task(1)
        self.assertEqual(result, "Task removed.")
        self.assertEqual(self.task_manager.get_task(1), "Task not found.")

    def test_remove_nonexistent_task(self):
        result = self.task_manager.remove_task(2)
        self.assertEqual(result, "Task not found.")

if __name__ == "__main__":
    unittest.main()
