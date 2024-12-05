def custom_generator():
    for el in range(2):
        yield el
    return 'Haleluya we have finished!'


cgi = iter(custom_generator())
print(next(cgi))
print(next(cgi))
# print(next(cgi))  # StopIteration error
#
#
def count_custom(start=0, step=1):
    # count(10) --> 10 11 12 13 14 ...
    # count(2.5, 0.5) --> 2.5 3.0 3.5 ...
    n = start
    while True:
        yield n
        n += step


nums = iter(count_custom(100, step=100))
print(next(nums))

# https://docs.python.org/3/library/itertools.html#itertools.count
from itertools import count

nums = iter(count(100, 10))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
