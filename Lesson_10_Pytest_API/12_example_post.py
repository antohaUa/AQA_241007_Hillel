import requests
url = 'http://jsonplaceholder.typicode.com/posts'
data_to_send = {'userId': 10, 'id': 101, 'title': 'Some title'}
response = requests.post(url, data=data_to_send)
# Перевірка статус-коду
if response.status_code == 201:
    created_data = response.json()
    # отримання даниху форматі JSON
    print('Створено дані:', created_data)
else:
    print('Помилка. Статус-код:', response.status_code)