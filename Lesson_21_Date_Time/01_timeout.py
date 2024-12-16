import time


def poll_event(check_function, timeout, interval=1):
    """
    Poll an event with retries during a defined timeout.

    Args:
        check_function (function): A function to check the desired condition. Should return True if the condition is met.
        timeout (int): Maximum time (in seconds) to keep polling.
        interval (int): Time (in seconds) to wait between retries.

    Returns:
        bool: True if the condition is met within the timeout, False otherwise.
    """
    start_time = time.time()

    while True:
        # Check the condition
        if check_function():
            return True

        # Check if timeout has been exceeded
        elapsed_time = time.time() - start_time
        if elapsed_time >= timeout:
            return False

        # Wait before the next retry
        time.sleep(interval)


# Example usage
import random


def random_condition():
    """Simulates a random condition that might succeed over time."""
    # Simulate a 20% chance of success each time this is called
    return random.random() < 0.2


if __name__ == "__main__":
    timeout = 10  # seconds
    interval = 2  # seconds

    print(f"Polling for a random condition with a timeout of {timeout} seconds...")
    result = poll_event(random_condition, timeout, interval)

    if result:
        print("Condition met within timeout!")
    else:
        print("Timeout exceeded before condition was met.")
