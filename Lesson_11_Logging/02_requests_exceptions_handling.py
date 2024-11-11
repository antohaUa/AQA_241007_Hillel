import requests
from requests.exceptions import HTTPError, Timeout

try:
    url = 'http://jsonplaceholder.typicode.com/404.html'
    response = requests.get(url, timeout=5)
    print(response.status_code)
    # response.raise_for_status()  # якщо код не 2xx (4xx, 5xx)
# except requests.exceptions.HTTPError as abc_err:
#     pass
except HTTPError as http_err:
    print('HTTP Помилка:', http_err)
except ConnectionError as conn_err:
    print('Connection error:', conn_err)
except Timeout as time_err:
    print('Часова помилка:', time_err)
except Exception as g_exc:
    print(g_exc)
finally:
    print('End')
