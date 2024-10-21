l0 = [1, 2, 34, 'hello', tuple(range(10))]
print(l0)
print(type(l0))

l1 = []
print(l1)
l0[0] = 3
l0[3] = 'abc'
print(l0)

l1 = [1, 2, 3]
my_var = l1.append(4)  # l1[len(l1):] = [4]
print(l1)
print(my_var)  # None
l1.append(5)
print(l1)
l1.insert(0, 6)
print(l1)

#######
size = 10
my_list1 = [None] * size
print(my_list1)
my_list0 = [1] * 10
print(my_list0)
print(type(my_list0))
my_list2 = list(range(10, 100, 5))
print(my_list2)
my_list3 = list('ABCDEFGHIJKLMNOP')
print(my_list3)

# my_list4 = list(1)  # 'int' object is not iterable   there is no __iter__ call
# print(my_list4)


first, second, *rest, last = [1, 2, 3, 4, 5, 6, 7, 8]
print(first)
print(second)
print(rest)
print(last)
print(type(rest))


def some_func(x):
    return x[1]


# indexes        0  1  2
print(some_func([1, 2, 3]))


# In [180]: l0.append([1,2,3])
#
# In [181]: l0
# Out[181]: [1, 2, 34, [1, 2, 3]]
#
# In [182]: l0 = [1, 2, 34]
#
# In [183]: l0.extend([1,2,3])
#
# In [184]: l0
# Out[184]: [1, 2, 34, 1, 2, 3]

