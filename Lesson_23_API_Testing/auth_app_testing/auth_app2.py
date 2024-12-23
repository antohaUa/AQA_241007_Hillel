from flask import Flask, request, jsonify, session
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Користувачі та їх паролі
users = {
    "admin": "adminpassword",
    "user": "userpassword"
}


# Функція для перевірки авторизації
def check_auth(username, password):
    return username in users and users[username] == password


# Декоратор для захисту маршрутів авторизацією
def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'username' not in session or not check_auth(session['username'], session.get('password')):
                return jsonify({'message': 'Authentication required!'}), 401
        return f(*args, **kwargs)

    return decorated


# Демонстраційний контент (ви можете замінити це на реальну базу даних)
content = []


# Маршрут для авторизації
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    if check_auth(data['username'], data['password']):
        session['username'] = data['username']
        session['password'] = data['password']
        return jsonify({'message': 'Logged in successfully!'})
    else:
        return jsonify({'message': 'Invalid credentials!'}), 401


# Маршрут для виходу
@app.route('/logout')
def logout():
    session.clear()
    return jsonify({'message': 'Logged out successfully!'})


# Маршрут для отримання контенту
@app.route('/content', methods=['GET'])
@require_auth
def get_content():
    return jsonify({'content': content})


# Маршрут для створення нового контенту
@app.route('/content', methods=['POST'])
@require_auth
def create_content():
    data = request.json
    content.append(data)
    return jsonify({'message': 'Content created successfully!'})


# Маршрут для оновлення існуючого контенту
@app.route('/content/<int:id>', methods=['PUT'])
@require_auth
def update_content(id):
    data = request.json
    content[id] = data
    return jsonify({'message': 'Content updated successfully!'})


# Маршрут для видалення існуючого контенту
@app.route('/content/<int:id>', methods=['DELETE'])
@require_auth
def delete_content(id):
    del content[id]
    return jsonify({'message': 'Content deleted successfully!'})


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 8080
    app.run(host=host, port=port, debug=True)
