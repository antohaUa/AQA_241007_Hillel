from flask import Flask, request
import logging
from logging.handlers import HTTPHandler

app = Flask(__name__)

# Configure the logger
logger = logging.getLogger('flask_app')
logger.setLevel(logging.DEBUG)

## Create a HTTPHandler to handle logs sent via HTTP POST
# http_handler = HTTPHandler('localhost:5000', '/log', method='POST')
# logger.addHandler(http_handler)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
logger.addHandler(console_handler)


# Route to receive log messages via HTTP POST
@app.route('/log', methods=['POST'])
def log():
    # Check Content-Type of the request
    content_type = request.headers.get('Content-Type', '')

    if content_type.startswith('application/json'):
        # If Content-Type is JSON, extract data using request.json
        content = request.json
    elif content_type.startswith('application/x-www-form-urlencoded'):
        # If Content-Type is form-urlencoded, extract data using request.form
        content = request.form.to_dict()
    else:
        return 'Unsupported Media Type', 415

    log_level = content.get('levelname', 'info').upper()
    message = content.get('msg', '')

    if log_level == 'DEBUG':
        logger.debug(f'[{log_level}] {message}')
    elif log_level == 'INFO':
        logger.info(f'[{log_level}] {message}')
    elif log_level == 'WARNING':
        logger.warning(f'[{log_level}] {message}')
    elif log_level == 'ERROR':
        logger.error(f'[{log_level}] {message}')
    elif log_level == 'CRITICAL':
        logger.critical(f'[{log_level}] {message}')

    return 'Log received successfully', 200


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 7070
    app.run(host=host, port=port, debug=True)
