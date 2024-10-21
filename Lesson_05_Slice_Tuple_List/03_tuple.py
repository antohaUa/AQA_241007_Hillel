# literal
# A
t1 = (1, 2, '3', bool(4), 5.505)
print(t1)
print(type(t1))

# B
t1_rare = 1, 2, '3'
print(t1_rare)
print(type(t1_rare))

# single element tuple
t3 = (10,)
print(t3)
print(type(t3))
#
v, w, x, y, z = t1
print(v, w, x, y, z)
print(z)
v1, *y1, z1 = t1
print(v1, y1, z1)
print(type(y1))

t10 = ('Adam', 'Surname', '1990', 'Engineer')
name, surname, birth_year, profession = t10

# indexes
#     0  1  2  3  4  5  6  7  8
t3 = (1, 1, 1, 2, 2, 3, 7, 3, 0)
# help('tuple.count')
print(t3.count(1))

# # index(self, value, start=0, stop=9223372036854775807, /)
# #  | Return first index of value.
print(t3.index(3, 6))
print(t3[4])

# tuple creation
# t4 = tuple(12)   # error int not iterable
# print(t4)

t5 = tuple('abc')
print(t5)

from string import ascii_lowercase

print(ascii_lowercase)
print(type(ascii_lowercase))

t6 = tuple(enumerate(ascii_lowercase, start=1))
print(t6)

# do not mix with generators
g1 = (itm for itm in t1 if itm != 2)
print(type(g1))

# named tuple
from collections import namedtuple

nt = namedtuple('Date', ['year', 'month', 'date'])

date1 = nt(2023, 6, 10)
date2 = nt(2023, 7, 7)
print(date2)
# print(dir(date2))
print(date2[0])
