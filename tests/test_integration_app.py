import unittest
from flask import Flask
from app import task_manager  # Assurez-vous que le chemin est correct
from app import app
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestIntegration(unittest.TestCase):

    def setUp(self):
        # Configurez l'application Flask pour les tests
        self.app = app.test_client()
        self.app.testing = True
        task_manager.TaskManager().users = {}  # Réinitialiser les utilisateurs pour chaque test

    def test_register_login_logout(self):
        # Test de l'inscription d'un nouvel utilisateur
        response = self.app.post('/register', data=dict(username="testuser", password="testpass"))
        self.assertEqual(response.status_code, 302)  # Redirection après l'inscription réussie

        # Test de la connexion
        response = self.app.post('/login', data=dict(username="testuser", password="testpass"))
        self.assertEqual(response.status_code, 302)  # Redirection après la connexion réussie

        # Vérifiez que la session contient le bon utilisateur
        with self.app as client:
            client.post('/login', data=dict(username="testuser", password="testpass"))
            with client.session_transaction() as session:
                self.assertEqual(session['username'], 'testuser')

        # Test de la déconnexion
        response = self.app.get('/logout')
        self.assertEqual(response.status_code, 302)  # Redirection après la déconnexion réussie

    def test_add_task(self):
        # Inscription et connexion de l'utilisateur
        self.app.post('/register', data=dict(username="testuser", password="testpass"))
        self.app.post('/login', data=dict(username="testuser", password="testpass"))

        # Ajout d'une nouvelle tâche
        response = self.app.post('/add_task', data=dict(task_id="1", description="Test task", priority="high"))
        self.assertEqual(response.status_code, 302)  # Redirection après l'ajout de tâche

        # Vérifiez que la tâche a été ajoutée
        response = self.app.get('/')
        self.assertIn(b"Test task", response.data)

    def test_mark_task_completed(self):
        # Inscription et connexion de l'utilisateur
        self.app.post('/register', data=dict(username="testuser", password="testpass"))
        self.app.post('/login', data=dict(username="testuser", password="testpass"))

        # Ajout d'une nouvelle tâche
        self.app.post('/add_task', data=dict(task_id="1", description="Test task", priority="high"))

        # Marquez la tâche comme complétée
        response = self.app.get('/mark_completed/1')
        self.assertEqual(response.status_code, 302)  # Redirection après avoir marqué la tâche comme complétée

        # Vérifiez que la tâche a été complétée
        tasks = task_manager.TaskManager().get_all_tasks()
        self.assertTrue(tasks["1"]["completed"])

    def test_delete_task(self):
        # Inscription et connexion de l'utilisateur
        self.app.post('/register', data=dict(username="testuser", password="testpass"))
        self.app.post('/login', data=dict(username="testuser", password="testpass"))

        # Ajout d'une nouvelle tâche
        self.app.post('/add_task', data=dict(task_id="1", description="Test task", priority="high"))

        # Supprimer la tâche
        response = self.app.get('/delete_task/1')
        self.assertEqual(response.status_code, 302)  # Redirection après la suppression de tâche

        # Vérifiez que la tâche a été supprimée
        tasks = task_manager.TaskManager().get_all_tasks()
        self.assertNotIn("1", tasks)

if __name__ == '__main__':
    unittest.main()
