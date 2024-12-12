from functools import wraps


def deco_params(**kwargs):
    def deco(func):
        @wraps(func)
        def new_function(*args):
            """New function doc."""
            print('Deco start')
            print(func.__doc__)
            print(func.__name__)
            strings_allowed = kwargs.get('strings_allowed')
            if not strings_allowed:
                if any(type(itm) == str for itm in args):
                    raise ValueError('Strings are not allowed')
            result = func(*args)
            print('Deco stop')
            return result

        return new_function

    return deco


@deco_params(strings_allowed=False)
def target_function(*args):
    """Some function."""
    print(f'Working OK with {args=}')


target_function(1, 2, 3, 5)
print(target_function.__doc__)
print(target_function.__name__)
