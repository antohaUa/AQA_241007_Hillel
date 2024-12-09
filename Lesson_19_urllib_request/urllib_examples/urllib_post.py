import urllib.request
import urllib.parse
import json

url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

# Convert data to JSON and encode it to bytes
json_data = json.dumps(data).encode("utf-8")

# Set headers
headers = {"Content-Type": "application/json"}

# Create a request object
request = urllib.request.Request(url, data=json_data, headers=headers, method="POST")

# Perform a POST request
with urllib.request.urlopen(request) as response:
    response_data = response.read()
    print(response_data.decode("utf-8"))