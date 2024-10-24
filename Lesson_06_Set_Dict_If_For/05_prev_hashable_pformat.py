# dict new value
d1 = dict()
d1['new_key'] = 'new_value'

# pformat
people = [
    ('Alice', 32, 100, 'Johnson', 'female'),
    ('Bob', 41, 200, 'Smith', 'male'),
    ('Charlie', 27, 150, 'Jones', 'male'),
    ('David', 52, 75, 'Williams', 'male'),
    ('Eve', 18, 300, 'Davis', 'female'),
    ('Frank', 33, 50, 'Taylor', 'male'),
    ('Grace', 42, 125, 'Clark', 'female'),
    ('Henry', 26, 225, 'Lewis', 'male'),
    ('Ivy', 38, 175, 'Moore', 'female'),
    ('Jack', 20, 140, 'Harris', 'male'),
    ('Kate', 37, 110, 'Miller', 'female'),
    ('Leo', 44, 90, 'Wilson', 'male'),
    ('Mae', 29, 180, 'Brown', 'female'),
    ('Nick', 51, 70, 'Davies', 'male'),
    ('Oliver', 18, 250, 'Collins', 'male'),
    ('Pete', 36, 160, 'Green', 'male'),
]
import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
)

# logging.info(people)
from pprint import pprint, pformat

# logging.info(f'\n{pformat(people)}')

print(people)
# print(*people, sep='\n')
pprint(people)

# dict before cpython 3.6
hash_tbl = [
    ('--', '--', '--'),
    (542403711206072985, 'two', 2),
    ('--', '--', '--'),
    (4677866115915370763, 'three', 3),
    ('--', '--', '--'),
    (-1182584047114089363, 'one', 1),
    ('--', '--', '--'),
    ('--', '--', '--')
]
#
# dict after cpython 3.6
hash_table = [None, 1, None, 2, None, 0, None, None]
entries = [
    (-1182584047114089363, 'one', 1),
    (542403711206072985, 'two', 2),
    (4677866115915370763, 'three', 3),
    ('--', '--', '--'),
    ('--', '--', '--')
]
print('\n' * 5)

# hashable
# fs1 = frozenset((1, [12,11], 3))
# print(fs1)
t1 = (1, [1, 2], 3)
print(t1)

d1 = {t1: 20}
# #
# s1 = {1, [5, 2], 3, 4}
# print(s1)
#
# # dict keys , set members should be hashable
