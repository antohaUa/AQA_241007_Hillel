# # named arguments
# # positional arguments
# def func1(x):
#     return x
#
#
# # l1 = lambda x: x


def swimming_pool_volume(length, width, height=3):
    print(f'L:{length}, W:{width}, H:{height}')
    return length * height * width


print(swimming_pool_volume(5, 2, 1))
print(swimming_pool_volume(5, 2))
print(swimming_pool_volume(width=5, length=1))
print(swimming_pool_volume(height=4, width=5, length=1))


# # print(swimming_pool_volume(height=4, width=5))


# # multiple values for argument restricted
#
# #################################
#
# def add_list_bad_example(val, l1=[]):  # arguments should be immutable
#     l1.append(val)
#     return l1


def add_list(val, l1=None):
    l1 = [] if l1 is None else l1
    l1.append(val)
    return l1


#
print(add_list(5, [1]))
print(add_list(6, [2, 3]))
print(add_list(5))
print(add_list(6))


#
#
##############################
#
def max_value(a, b, *args):
    # print(a)
    # print(b)
    print(args)
    print(type(args))
    return max(a, b, *args)


print(max_value(1, 5))
print(max_value(b=1, a=5))
print(max_value(1, 4, 17, 3, 18))


#

def max_value2(*args):
    print(*args)
    pass


print(max_value2(1, 5))
print(max_value2())


def kwargs_example(a, *args, **kwargs):
    print(a)
    print(args)
    # print(lenght)
    print(kwargs)
    print(type(kwargs))
    print(kwargs.get('color'), 'Default')
    return {**kwargs, 'custom': True}


#

print(kwargs_example(5, {1: 23}, [1, 2, 3], lenght=10, color='red', width={2: 24}))
d1 = {'lenght': 10, 'color': 'red', 'width': {2: 24}}
print(kwargs_example(5, lenght=d1))
print(kwargs_example(5, **d1))


def some_example(*, a, **kwargs):
    print(a)
    print(kwargs)


some_example(a=1, b=14)


#
# some_example(1)
#
# *
def func(a, *, b, c):
    print(a, b, c)
    # a - positional
    # b, c -named
#
#
# # func(1, c=2, b=3)
# # # func(1)
# # # func(1, 2, 3)
