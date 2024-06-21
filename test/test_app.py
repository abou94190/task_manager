import unittest
import sys , os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.task_manager import app
from flask import Flask, session

from flask_testing import TestCase

class MyTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SECRET_KEY'] = 'your_secret_key'
        return app

    def setUp(self):
        task_manager.clear_tasks()  # Assuming you have a method to clear all tasks for testing purposes
        task_manager.clear_users()  # Assuming you have a method to clear all users for testing purposes

    def tearDown(self):
        pass

    def test_index_redirect_if_not_logged_in(self):
        response = self.client.get('/')
        self.assert_redirects(response, '/login')

    def test_login(self):
        with self.client:
            response = self.client.post('/login', data=dict(username='testuser', password='testpass'))
            self.assert_template_used('login.html')
            self.assertIn(b'Login successful.', response.data)

    def test_register(self):
        with self.client:
            response = self.client.post('/register', data=dict(username='testuser', password='testpass'))
            self.assert_redirects(response, '/login')
            response = self.client.post('/login', data=dict(username='testuser', password='testpass'))
            self.assert_template_used('login.html')
            self.assertIn(b'Login successful.', response.data)

    def test_logout(self):
        with self.client:
            self.client.post('/login', data=dict(username='testuser', password='testpass'))
            response = self.client.get('/logout')
            self.assert_redirects(response, '/login')
            self.assertNotIn('username', session)

    def test_add_task(self):
        with self.client:
            self.client.post('/register', data=dict(username='testuser', password='testpass'))
            self.client.post('/login', data=dict(username='testuser', password='testpass'))
            response = self.client.post('/add_task', data=dict(task_id='1', description='Test Task', priority='High'))
            self.assert_redirects(response, '/')
            tasks = task_manager.get_all_tasks()
            self.assertEqual(len(tasks), 1)
            self.assertEqual(tasks[0]['description'], 'Test Task')

    def test_mark_completed(self):
        with self.client:
            self.client.post('/register', data=dict(username='testuser', password='testpass'))
            self.client.post('/login', data=dict(username='testuser', password='testpass'))
            self.client.post('/add_task', data=dict(task_id='1', description='Test Task', priority='High'))
            response = self.client.get('/mark_completed/1')
            self.assert_redirects(response, '/')
            tasks = task_manager.get_all_tasks()
            self.assertTrue(tasks[0]['completed'])

    def test_delete_task(self):
        with self.client:
            self.client.post('/register', data=dict(username='testuser', password='testpass'))
            self.client.post('/login', data=dict(username='testuser', password='testpass'))
            self.client.post('/add_task', data=dict(task_id='1', description='Test Task', priority='High'))
            response = self.client.get('/delete_task/1')
            self.assert_redirects(response, '/')
            tasks = task_manager.get_all_tasks()
            self.assertEqual(len(tasks), 0)

if __name__ == '__main__':
    unittest.main()


