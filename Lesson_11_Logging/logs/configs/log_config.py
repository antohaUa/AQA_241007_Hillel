import logging.config
import json


def setup_logging():
    with open('logging_config.json', 'r') as fh:
        config = json.load(fh)
        logging.config.dictConfig(config)


if __name__ == '__main__':
    setup_logging()
    # Example usage of the logger
    logger = logging.getLogger(__name__)
    logger.debug('This is a debug message')
    logger.info('This is an information message')
    logger.warning('This is a warning')
    logger.error('This is an error message')
    logger.critical('This is a critical error')
