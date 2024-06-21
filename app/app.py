# app/app.py

from flask import Flask
from app.task_manager import TaskManager

app = Flask(__name__)

# Exemple d'utilisation de TaskManager dans votre application Flask
@app.route('/')
def index():
    task_manager = TaskManager()
    tasks = task_manager.get_all_tasks()
    # Manipulation des tâches ici
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
