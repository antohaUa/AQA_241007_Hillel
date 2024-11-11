import logging
from logging.handlers import HTTPHandler
import requests

# Configure logging to send logs via HTTP POST
logger = logging.getLogger('client_logger')
logger.setLevel(logging.DEBUG)

# Create a HTTPHandler to send logs via HTTP POST to Flask server
http_handler = HTTPHandler('localhost:7070', '/log', method='POST')
logger.addHandler(http_handler)

# Log messages using different log levels
logger.debug('This is a debug message from the client')
logger.info('This is an info message from the client')
logger.warning('This is a warning message from the client')
logger.error('This is an error message from the client')
logger.critical('This is a critical message from the client')

# Send log messages via HTTP POST to Flask server
requests.post('http://localhost:7070/log', json={'levelname': 'DEBUG', 'msg': 'Custom Message'})
