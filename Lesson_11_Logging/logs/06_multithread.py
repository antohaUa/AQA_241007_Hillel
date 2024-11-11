import logging
import threading
import time


# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(threadName)s - %(levelname)s - %(message)s')


# Function to be executed by each thread
def thread_function():
    logging.debug("Starting")
    # print("Starting")
    time.sleep(1)  # Simulating some initial work
    logging.debug("Middle of execution")
    # print("Middle of execution")
    time.sleep(1)  # Simulating some more work
    logging.debug("Exiting")
    # print("Exiting")


if __name__ == "__main__":
    threads = []
    for i in range(7):
        thread = threading.Thread(target=thread_function)
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    logging.debug("All threads have finished")
    # print("All threads have finished")
