import time
import urllib.request
import requests

# URL for testing
url = "https://jsonplaceholder.typicode.com/posts/1"

# Number of iterations to measure
iterations = 100


def speed_urllib():
    """Measure the time taken by urllib to make GET requests."""
    start_time = time.time()
    for _ in range(iterations):
        with urllib.request.urlopen(url) as response:
            response.read()
    end_time = time.time()
    return end_time - start_time


def speed_requests():
    """Measure the time taken by requests to make GET requests."""
    start_time = time.time()
    for _ in range(iterations):
        response = requests.get(url)
        response.text  # Read response text to simulate processing
    end_time = time.time()
    return end_time - start_time


if __name__ == '__main__':
    # Run the tests
    requests_time = speed_requests()
    urllib_time = speed_urllib()

    # Print results
    print(f"Time taken by urllib for {iterations} requests: {urllib_time:.2f} seconds")
    print(f"Time taken by requests for {iterations} requests: {requests_time:.2f} seconds")

    # Compare the results
    print("urllib is faster.") if urllib_time < requests_time else print("requests is faster.")
