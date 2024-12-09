# Given function that accepts positional arguments
# write decorator that will accept params strings_allowed=True/False
# and raise Value Error in case unfulfilled condition

def deco_params(**kwargs):
    def deco(func):
        def new_function(*args):
            print('Deco start')
            print(func.__doc__)
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
# target_function(1, 2, 4, 's', 8, 0)
