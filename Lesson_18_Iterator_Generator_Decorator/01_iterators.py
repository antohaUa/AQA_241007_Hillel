# https://docs.python.org/3/library/functions.html#iter

for itm in range(1, 6):
    print(itm)

s1 = 'Hi!'
s1_iterator = iter(s1)
s2_iterator = s1.__iter__()
print(type(s1_iterator))
print(type(s2_iterator))
#
# # 'int' object is not iterable
# i1 = 23134
# itr1 = iter(i1)
# print(itr1)

t1 = ("⛵", "🚓", "🛵")
# print(len(t1))
t1_iterator = iter(t1)
# print(type(t1_iterator))
# #
print(t1_iterator.__next__())
print(next(t1_iterator))
print(next(t1_iterator))
# print(next(t1_iterator))  # here will be StopIteration error
# to avoid this error we able to use default value or try-except errors handling
print(next(t1_iterator, 'some default value'))
#
# try:
#     print(next(t1_iterator))
#     print(next(t1_iterator))
#     print(next(t1_iterator))
#     print(next(t1_iterator))
# except StopIteration as s_err:
#     print(s_err.value)
#     print("Let's be silent")
#     print('we start use iterator second time')
#     for el in t1_iterator:
#         print(el)  # here no prints cause iterator was stopped
#     print('-' * 20)
#
# en1 = iter(enumerate('Hi!', start=10))
# print(next(en1))
# print(next(en1))
# print(next(en1))
#
# t1 = ['🚲', "⛵", "🚓", "🛵"]
# t1_iter = iter(t1)
# print(next(t1_iter))
# t1.insert(2, '🚲')
# print(next(t1_iter))
# print(next(t1_iter))
# print(next(t1_iter))
#
# # iterators sizes
# my_str = ''
# my_list = []
# my_tuple = ()
# my_bytes = b''
# my_bytearray = bytearray()
# my_set = set()
# my_frozenset = frozenset()
# my_dict = dict()
# my_range = range(0)
# import sys
#
# print(sys.getsizeof(iter(my_str)))
# print(my_str.__sizeof__())
# print('-' * 20)
# print('-' * 20)
# print(sys.getsizeof(iter(my_list)))
# print(my_list.__sizeof__())
# print('-' * 20)
# print(sys.getsizeof(iter(my_tuple)))
# print(my_tuple.__sizeof__())
# print('-' * 20)
# print(sys.getsizeof(iter(my_bytes)))
# print(sys.getsizeof(iter(my_bytearray)))
# print(sys.getsizeof(iter(my_set)))
# print(sys.getsizeof(iter(my_frozenset)))
# print(sys.getsizeof(iter(my_dict)))
# print(iter(my_range).__sizeof__())
#
# # itertools
#  https://docs.python.org/3/library/itertools.html

from itertools import permutations, groupby

l1 = [1, 2, 3, 4]
iterator1 = permutations(l1, 4)
for el in iterator1:
    print(el)

s1 = 'AAAABBBCCDAABBBBBBBBBBBBB'
s1_iter = groupby(s1)
for el, val in s1_iter:
    # print(el)
    print(''.join(list(val)))
