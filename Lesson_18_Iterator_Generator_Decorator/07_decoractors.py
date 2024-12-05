def deco(func):
    def wrapper(*args, **kwargs):
        print('**' * 30)
        v = func(*args, **kwargs) * 10
        print('$-' * 30)
        return v

    return wrapper


def deco2(func):
    def wrapper(a, b):
        print('=' * 30)
        v = func(a, b) * 2
        print('==' * 30)
        return v

    return wrapper


#
@deco
def target_func(v1, v2):
    print('Creating tuple:')
    return (v1, v2)


#
val = target_func(1, 2)
print(val)

# decorator use without annotation
internal_function = deco(target_func)
val2 = internal_function(1, 2)
print(val2)

# measure time
import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.monotonic()
        val = func(*args, **kwargs)
        end = time.monotonic()
        print(f'Time:{end - start:.5f} sec')
        return val

    return wrapper


@measure_time
def create_list(range_num):
    print('Function start')
    return list(range(range_num))


# # decorator use without annotation
# # upgraded_function = measure_time(create_list)
# # upgraded_function(80_000_000)

create_list(80_000_000)

