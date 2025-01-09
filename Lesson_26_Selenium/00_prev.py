import requests
from requests.exceptions import HTTPError, Timeout


def do_request(method, url, **kwargs):
    try:
        response = getattr(requests, method)(url, **kwargs)
        # response = requests.'get'(url, timeout=5)
        print(response.status_code)
        response.raise_for_status()  # якщо код не 2xx (4xx, 5xx)
        return response
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


if __name__ == '__main__':
    # url = 'http://jsonplaceholder.typicode.com/posts/1/comments'



    # url = 'http://jsonplaceholder.typicode.com/posts/1'
    # params = {'userId': 10, 'id': 101, 'title': 'New title'}
    # headers = {'User-Agent': 'MyHeader', 'Content-Type': 'text/html'}

    url = 'http://jsonplaceholder.typicode.com/404.html'
    do_request('get', url=url, timeout=5)

    url2 = 'http://jsonplaceholder.typicode.com/posts'
    data_to_send = {'userId': 10, 'id': 101, 'title': 'Some title'}
    curr_response = do_request('post', url=url2, timeout=5, data=data_to_send)
    print(curr_response.text)
