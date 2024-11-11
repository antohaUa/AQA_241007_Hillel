import logging

from child_log import child_call

# Create the parent logger
parent_logger = logging.getLogger('Main')
parent_logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Create a handler for the parent logger
parent_handler = logging.StreamHandler()
# Apply the formatter to the handler
parent_handler.setFormatter(formatter)
parent_handler.setLevel(logging.DEBUG)
parent_logger.addHandler(parent_handler)


def parent_call():
    parent_logger.info('This is parent call')


if __name__ == '__main__':
    import sys

    # Displaying the current search paths
    # print("Current search paths:")
    # for path in sys.path:
    #     print(path)
    # print('-' * 40)
    parent_call()
    child_call()
