def decorator_function(original_function):
    """
    A decorator function that wraps the original function and adds additional functionality to it.

    Args:
        original_function (func): The original function to be decorated.

    Returns:
        func: The decorated function.
    """

    def wrapper_function(*args, **kwargs):
        """
        A wrapper function that executes the original function and adds some extra functionality before and/or after it.

        Args:
            *args: Positional arguments passed to the original function.
            **kwargs: Keyword arguments passed to the original function.

        Returns:
            The return value of the original function.
        """
        # Add extra functionality before calling the original function
        print(f'Wrapper function is executing before calling {original_function.__name__}')

        result = original_function(*args, **kwargs)  # Call the original function

        # Add extra functionality after calling the original function
        print(f'Wrapper function is executing after calling {original_function.__name__}')

        return result

    return wrapper_function


# our custom decorator
def deco2(func):
    def wrapper(name):
        upper_name = str(name).upper()
        print(f'Hello, {upper_name}!')

    return wrapper


@decorator_function
# @deco2
def greet(name):
    """
    A function that greets the given name.

    Args:
        name (str): The name of the person to greet.
    """
    print(f'Hello, {name}!')
    # return f'Hello, {name}!'   # best practice


# Test the decorated function
greet('Alice')
