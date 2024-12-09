import requests

# # # Відкриття файлу для завантаження
# with open('file_to_upload.txt', 'rb') as file:
#     files = {'file': file}
#     # Виконання POST-запиту з файлом
#     response = requests.post('https://example.com/upload', files=files)
#     # Обробка відповіді
#     print(response.text)


url = 'https://httpbin.org/post'

multiple_files = [
    ('images', ('man.png', open('man.png', 'rb'), 'image/png')),
    ('images', ('download.png', open('download.png', 'rb'), 'image/png'))]

r = requests.post(url, files=multiple_files)
print(r.text)

