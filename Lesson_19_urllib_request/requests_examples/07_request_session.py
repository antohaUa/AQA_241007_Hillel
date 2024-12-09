import requests

# # A
# response = requests.get('https://httpbin.org/cookies/set/sessioncookie/1234')
# print(response.text)
#
# # B   - independent session without any relation with A request
# response2 = requests.get('https://httpbin.org/cookies')
# print(response2.text)

#
# session = requests.Session()
# r1 = session.get('https://httpbin.org/cookies/set/sessioncookie/1234')
# print(r1.json())
#
# # this request has relations with previous one
# r2 = session.get('https://httpbin.org/cookies')
# print(r2.json())  # '{"cookies": {"sessioncookie": "1234"}}'

import requests
from requests.adapters import HTTPAdapter

# # Створення сесії
# session = requests.Session()
# adapter = HTTPAdapter(max_retries=3)
# # Додавання адаптера до сесії
# session.mount('http://', adapter)
# session.mount('https://', adapter)
# # Виконання запиту з встановленим таймаутом
# response = session.get('https://example.com')
# print(response.status_code)

# session pool
session = requests.Session()
adapter = requests.adapters.HTTPAdapter(
    pool_connections=10,
    pool_maxsize=100)
session.mount('http://', adapter)
response4 = session.get("http://example.org")
print(response4.status_code)
print(response4.text)
