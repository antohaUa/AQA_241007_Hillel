# create variables and then print
print('Some text')

l1 = [1, 2, 3]
print(*l1, sep='\n')

x1 = f'{l1[0]} - {l1[1]}'
# breakpoint()
print(x1)

# string new value
# In [1]: s1 = 'Hello world!'
#
# In [2]: l1 = s1.split()
#
# In [3]: l1
# Out[3]: ['Hello', 'world!']
#
# In [4]: l1.insert(1, 'Big')
#
# In [5]: l1
# Out[5]: ['Hello', 'Big', 'world!']
#
# In [6]: ' '.join(l1)
# Out[6]: 'Hello Big world!'


# dict new value
d1 = dict()
d1['b'] = 4
d1.get('b', 'default')

# split
s1 = '15432grn'

import string

int(s1.rstrip(string.ascii_lowercase))
