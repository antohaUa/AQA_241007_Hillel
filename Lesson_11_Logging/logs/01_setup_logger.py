import logging



def setup_logger():
    # Create a logger object
    logger = logging.getLogger('Main')
    #_log = logging.getLogger('Main')

    # Set the logging level for the logger
    logger.setLevel(logging.DEBUG)

    # Create a formatter for the logs
    formatter = logging.Formatter('%(asctime)s -> %(name)s - [%(levelname)s] - %(message)s')

    # Create a handler for logging to the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)  # Set the logging level for the handler
    console_handler.setFormatter(formatter)  # Apply the formatter to the handler

    # Create a handler for logging to file
    file_handler = logging.FileHandler(filename='01.log', mode='a')
    file_handler.setLevel(logging.DEBUG)  # Set the logging level for the handler
    file_handler.setFormatter(formatter)  # Apply the formatter to the handler

    # Add the handler to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


if __name__ == '__main__':
    logger = setup_logger()
    # Example usage of the logger
    logger.debug('This is a debug message')
    logger.info('This is an information message')
    logger.warning('This is a warning')
    logger.error('This is an error message')
    logger.critical('This is a critical error')
