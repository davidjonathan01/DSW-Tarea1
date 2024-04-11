from flask import abort
from flask import Flask

app = Flask(__name__)

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

# Función de ejemplo para cargar un usuario
def load_user(user_id):
    # Aquí puedes implementar la lógica para cargar el usuario desde alguna fuente de datos, como una base de datos
    # Por simplicidad, aquí solo se crea un usuario ficticio
    users = {
        '1': User('1', 'David'),
        '2': User('2', 'Jonathan'),
        '3': User('3', 'Maria')
    }
    return users.get(user_id)

@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, %s</h1>' % user.name

if __name__ == '__main__':
    app.run(debug=True)
