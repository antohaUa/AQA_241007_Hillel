import requests

url = 'http://jsonplaceholder.typicode.com/posts/1'
params = {'userId': 10, 'id': 101, 'title': 'New title'}
headers = {'User-Agent': 'MyHeader', 'Content-Type': 'text/html'}
response = requests.delete(url, params=params, headers=headers, timeout=10)
# Перевірка статус-коду
if response.status_code == 200:
    print(response.request.headers)
    print('Дані успішно видалено')
else:
    print('Помилка. Статус-код:', response.status_code)
