from flask import Flask, jsonify, request
from task_manager import TaskManager

app = Flask(__name__)
task_manager = TaskManager()

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    task_id = data.get('task_id')
    description = data.get('description')
    result = task_manager.add_task(task_id, description)
    return jsonify({'message': result})

@app.route('/tasks/<task_id>', methods=['GET'])
def get_task(task_id):
    result = task_manager.get_task(task_id)
    if result == "Task not found.":
        return jsonify({'message': result}), 404
    return jsonify({'task': {task_id: result}})

@app.route('/tasks/<task_id>', methods=['DELETE'])
def remove_task(task_id):
    result = task_manager.remove_task(task_id)
    if result == "Task not found.":
        return jsonify({'message': result}), 404
    return jsonify({'message': result})

if __name__ == '__main__':
    app.run(debug=True)