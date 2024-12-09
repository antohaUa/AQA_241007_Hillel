import urllib.request

url = "https://jsonplaceholder.typicode.com/posts/1"

# Perform a GET request
with urllib.request.urlopen(url) as response:
    data = response.read()
    print(data.decode("utf-8"))