import logging
from logging.handlers import RotatingFileHandler

# Configure rotating log handler
log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
log_file = '03.log'

# Rotating log handler with a maximum of 5 backup files, each with a maximum size of 100 bytes
rotating_handler = RotatingFileHandler(filename=log_file, mode='a', maxBytes=100, backupCount=5)
rotating_handler.setFormatter(log_formatter)

# Add rotating handler to the logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(rotating_handler)

# Example usage of logging
logger.info(f'This is an informational message.\n{"=" * 50}')
logger.warning('This is a warning message.')
