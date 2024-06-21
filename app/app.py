from flask import Flask, render_template, request, redirect, url_for, session

from app.task_manager import TaskManager  # Assuming TaskManager is in a separate file

app = Flask(__name__)
task_manager = TaskManager()


@app.route('/')
def index():
    if 'username' in session:
        tasks = task_manager.get_all_tasks()
        return render_template('index.html', tasks=tasks)
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        result = task_manager.login(username, password)
        if result == "Login successful.":
            session['username'] = username
            return redirect(url_for('index'))
        return render_template('login.html', error=result)
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        result = task_manager.register(username, password)
        if result == "User registered.":
            return redirect(url_for('login'))
        return render_template('register.html', error=result)
    return render_template('register.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    task_manager.logout()
    return redirect(url_for('login'))


@app.route('/add_task', methods=['POST'])
def add_task():
    if 'username' in session:
        task_id = request.form['task_id']
        description = request.form['description']
        priority = request.form['priority']
        task_manager.add_task(task_id, description, priority)
    return redirect(url_for('index'))

@app.route('/mark_completed/<task_id>')
def mark_completed(task_id):
    if 'username' in session:
        task_manager.mark_task_completed(task_id)
    return redirect(url_for('index'))


@app.route('/delete_task/<task_id>')
def delete_task(task_id):
    if 'username' in session:
        task_manager.remove_task(task_id)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)