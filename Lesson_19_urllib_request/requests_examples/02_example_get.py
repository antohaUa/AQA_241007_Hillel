import requests

# url = 'http://jsonplaceholder.typicode.com/posts/1/comments'
# response = requests.get(url)
#
# # Перевірка статус-коду
# if response.status_code == 200:
#     data = response.json()  # отримання даних у форматі JSON
#     print('Отримано дані:', data)
# else:
#     print('Помилка. Статус-код:', response.status_code)


# Parameters

url = 'http://jsonplaceholder.typicode.com/posts/1/comments'
params = {'postId': 1, 'email': 'Nikita@garfield.biz'}
response = requests.get(url, params=params)
if response.status_code == 200:
    data = response.json()
    print(response.request.headers)
    print(data)
    print(response.text)
    print(response.content)
else:
    print('Помилка запиту:', response.status_code)