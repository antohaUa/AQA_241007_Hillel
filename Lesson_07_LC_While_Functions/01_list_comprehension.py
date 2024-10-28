# https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
# task from target list of int create list of doubled values
l1 = [2, 4, 6, 8, 10]
new_l = []
for itm in l1:
    new_l.append(itm * 2)
print(new_l)

new_l2 = [element * 2 for element in l1]
print(new_l2)
#
# ############################################################

new_l3 = [1 for _ in l1]
print(new_l3)

#
# #
# # # syntax
# # temporary variables inside list comprehensions
s1 = 'abcceeedffff'
lc2 = [(ch, s1.count(ch)) for ch in s1]

print(lc2)
#
# In [43]: lc2 = [(ch, s1.count(ch)) for ch in sorted(list(set(s1)))]
#
# In [44]: lc2
# Out[44]: [('a', 1), ('b', 1), ('c', 2), ('d', 1), ('e', 3), ('f', 4)]

# https://docs.python.org/3/library/itertools.html

from itertools import groupby

# ('a', <itertools._grouper object at 0x7f70598c3cd0>)
# ('b', <itertools._grouper object at 0x7f70597cb250>)
# ('c', <itertools._grouper object at 0x7f70598c3cd0>)
# ('e', <itertools._grouper object at 0x7f70597cb250>)
# ('d', <itertools._grouper object at 0x7f70598c3cd0>)
# ('f', <itertools._grouper object at 0x7f70597cb250>)
lc2_grouped = [s1.count(key) for key, _ in groupby(s1)]
print(lc2_grouped)

l1 = [2, 4, 6, 3, 10]
#          statement      for cycle      if condition
new_l4 = [element * 2 for element in l1 if element * 2 <= 10]
print(new_l4)

# how to copy list
l2 = [el for el in l1]
# l2 = l1.copy()
# l2 = l1[:]
# [*l2] = l1
#
#          statement                             for cycle             if condition ( optional)
lc3 = [(x, 'even') if x % 2 == 0 else (x, 'odd') for x in range(1, 11) if x >= 5]
print(lc3)
#
# # for -> statement -> condition
#
# 1.1  1.2  1.3  1.4 .. 2.0
lc1 = [itm / 10 for itm in range(11, 21) if itm / 10 <= 1.5]
print(lc1)
#
# # https://docs.python.org/3/library/itertools.html#itertools.groupby
from itertools import groupby

lc2 = [list(group) for _, group in groupby('AAAABBBCCDEEFFFFFFF')]
print(*lc2, sep='\n')

# example: find all numbers 1-30 that have no digit 3 inside
l5 = [i for i in range(1, 31) if '3' not in str(i)]
