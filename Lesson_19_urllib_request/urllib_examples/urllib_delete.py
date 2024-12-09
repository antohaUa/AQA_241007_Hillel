import urllib.request

url = "https://jsonplaceholder.typicode.com/posts/1"

# Create a request object
request = urllib.request.Request(url, method="DELETE")

# Perform a DELETE request
with urllib.request.urlopen(request) as response:
    response_data = response.read()
    print(response_data.decode("utf-8"))