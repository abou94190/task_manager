from flask import Flask, render_template, request, redirect, url_for, session
from task_manager import TaskManager  # On suppose que TaskManager est dans un fichier séparé

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Clé secrète pour la gestion des sessions

task_manager = TaskManager()  # Instanciation du gestionnaire de tâches

@app.route('/')
def index():
    # Page d'accueil, redirige vers la page de connexion si l'utilisateur n'est pas connecté
    if 'username' in session:
        tasks = task_manager.get_all_tasks()
        return render_template('index.html', tasks=tasks)
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    # Route pour la connexion, gère à la fois l'affichage du formulaire et la soumission
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
    # Route pour l'inscription, gère à la fois l'affichage du formulaire et la soumission
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
    # Route pour la déconnexion, supprime l'utilisateur de la session
    session.pop('username', None)
    task_manager.logout()
    return redirect(url_for('login'))


@app.route('/add_task', methods=['POST'])
def add_task():
    # Route pour ajouter une tâche, vérifie si l'utilisateur est connecté
    if 'username' in session:
        task_id = request.form['task_id']
        description = request.form['description']
        priority = request.form['priority']
        task_manager.add_task(task_id, description, priority)
    return redirect(url_for('index'))

@app.route('/mark_completed/<task_id>')
def mark_completed(task_id):
    # Route pour marquer une tâche comme complétée, vérifie si l'utilisateur est connecté
    if 'username' in session:
        task_manager.mark_task_completed(task_id)
    return redirect(url_for('index'))


@app.route('/delete_task/<task_id>')
def delete_task(task_id):
    # Route pour supprimer une tâche, vérifie si l'utilisateur est connecté
    if 'username' in session:
        task_manager.remove_task(task_id)
    return redirect(url_for('index'))


if __name__ == '__main__':
    # Exécute l'application en mode debug
    app.run(debug=True)
