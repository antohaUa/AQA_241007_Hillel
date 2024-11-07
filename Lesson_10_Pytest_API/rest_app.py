from flask import Flask, request, jsonify, session
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Демонстраційний контент (ви можете замінити це на реальну базу даних)
content = []


# Маршрут для отримання контенту
@app.route('/content', methods=['GET'])
def get_content():
    return jsonify({'content': content})


# Маршрут для створення нового контенту
@app.route('/content', methods=['POST'])
def create_content():
    data = request.json
    content.append(data)
    return jsonify({'message': 'Content created successfully!'})


# Маршрут для оновлення існуючого контенту
@app.route('/content/<int:id>', methods=['PUT'])
def update_content(id):
    data = request.json
    content[id] = data
    return jsonify({'message': 'Content updated successfully!'})


# Маршрут для видалення існуючого контенту
@app.route('/content/<int:id>', methods=['DELETE'])
def delete_content(id):
    del content[id]
    return jsonify({'message': 'Content deleted successfully!'})


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 7070
    app.run(host=host, port=port, debug=True)
