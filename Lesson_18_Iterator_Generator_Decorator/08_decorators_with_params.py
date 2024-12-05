# decorators with parameters
def deco_params(ch='$', print_len=10):
    def deco_simple(func):
        def wrapper(*args, **kwargs):
            print(ch * print_len)
            v = func(*args, **kwargs)
            print(ch * print_len)
            return v

        return wrapper

    return deco_simple


@deco_params(ch='%^', print_len=10)
def _x1(x):
    """Some doc1."""
    print(x)
    return x


_x1(10)
