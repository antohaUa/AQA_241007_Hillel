import logging

logging.basicConfig(filename='02.log', level=logging.ERROR, filemode='w')


def divide_numbers(x, y):
    try:
        return x / y
    except ZeroDivisionError as z_exc:
        logging.exception("Division by zero occurred")
        # logging.error("Division by zero occurred")


result = divide_numbers(10, 0)
