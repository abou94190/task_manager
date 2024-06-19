import unittest
from app.task_manager import TaskManager


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.tm = TaskManager()

    def testaddtask(self):
        result = self.tm.addtask('1', 'Test task')
        self.assertEqual(result, 'Task added.')
        self.assertIn('1', self.tm.tasks)

    def test_add_task_existing_id(self):
        self.tm.add_task('1', 'Test task')
        result = self.tm.add_task('1', 'Another task')
        self.assertEqual(result, 'Task ID already exists.')

    def test_get_task(self):
        self.tm.add_task('1', 'Test task')
        result = self.tm.get_task('1')
        self.assertEqual(result, 'Test task')

    def test_get_task_not_found(self):
        result = self.tm.get_task('999')
        self.assertEqual(result, 'Task not found.')

    def test_remove_task(self):
        self.tm.add_task('1', 'Test task')
        result = self.tm.remove_task('1')
        self.assertEqual(result, 'Task removed.')
        self.assertNotIn('1', self.tm.tasks)

    def test_remove_task_not_found(self):
        result = self.tm.remove_task('999')
        self.assertEqual(result, 'Task not found.')


if __name__ == '__main':
    unittest.main()