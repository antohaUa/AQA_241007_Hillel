import requests
url = 'http://jsonplaceholder.typicode.com/posts/1'
data_to_send = {'userId': 10, 'id': 101, 'title': 'New title'}
response = requests.put(url, data=data_to_send)
# Перевірка статус-коду
if response.status_code == 200:
    updated_data = response.text  # отримання даних у форматі текст
    print('Оновлено дані:', updated_data)
else:
    print('Помилка. Статус-код:', response.status_code)