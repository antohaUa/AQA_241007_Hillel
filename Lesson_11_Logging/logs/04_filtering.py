import logging

# Define sensitive data
username = 'john_doe'
password = 'secret_password'

# Initialize logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


# Define a filter function to mask sensitive data
def mask_sensitive_data(record):
    if hasattr(record, 'msg'):
        record.msg = record.msg.replace(username, '<username>').replace(password, '<********>')
    return True


# Create a StreamHandler
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)

# Add the filter function to the StreamHandler
stream_handler.addFilter(mask_sensitive_data)

# Set the formatter for the StreamHandler
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(formatter)

# Add the StreamHandler to the logger
logger.addHandler(stream_handler)

# Log a message containing sensitive data
logger.info('Some text without secret data')
logger.info(f"Login attempt by user '{username}' with password '{password}'")
