# https://docs.python.org/3/library/collections.html#collections.deque
from collections import deque
from time import perf_counter_ns

TIMES = 10_000
a_list = []
a_deque = deque()


def average_time(func, times):
    total = 0.0
    for i in range(times):
        start = perf_counter_ns()
        func(i)
        total += perf_counter_ns() - start
    return total / times


list_time_insert = average_time(lambda i: a_list.insert(0, i), TIMES)
deque_time_appendleft = average_time(lambda i: a_deque.appendleft(i), TIMES)
gain = list_time_insert / deque_time_appendleft

print(f'list.insert()      {list_time_insert:.6} ns')
print(f'deque.appendleft() {deque_time_appendleft:.6} ns  ({gain:.6}x faster)')
print('-' * 50)

list_time_pop0 = average_time(lambda i: a_list.pop(0), TIMES)
deque_time_popleft = average_time(lambda i: a_deque.popleft(), TIMES)

gain_pop = list_time_pop0 / deque_time_popleft
print(f'list.pop(0)      {list_time_pop0:.6} ns')
print(f'deque.popleft() {deque_time_popleft:.6} ns  ({gain_pop:.6}x faster)')

# rotate method

print('=' * 30)
l1 = [1, 2, 3, 4]
d1 = deque(l1)
d1.rotate(1)
print(d1)
d1.rotate(-11)
print(d1)
