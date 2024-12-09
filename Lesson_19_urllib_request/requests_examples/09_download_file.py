import requests

# Виконання GET-запиту для скачування файлу
response = requests.get('https://www.pngall.com/wp-content/uploads/8/Sample-PNG-Image.png')
# Запис файлу на диск

with open('download.png', 'wb') as file:
    file.write(response.content)
