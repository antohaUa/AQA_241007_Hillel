# functions

# internal functions
# https://docs.python.org/uk/3.9/library/functions.html


# name is smth aka reference to function object
# print = 'asdasd'    # too bad !!!!!! cause we re-define core print function here

new_print = print  # possible cause we create aka "copy" of print function
print(type(new_print))
new_print()  # <- operator of function call
new_print('123')
print('124')


#
# # ###################################   Purpose
# # # DRY  - Don't Repeat Yourself
# #
# #
# simple_func(5)   # will not work. Function should be defined before function call !!!
def simple_func(x):
    print(x)
    # return None    # default return value is None even if return was not defined


simple_func(5)


#
#
# result = simple_func(5)
# print(result)  # <- None
# pass
# simple_func(5)
# pass
# simple_func(5)
#
#
# # # return
def func_with_return(x):
    result = x ** 2
    if result <= 100:
        return result
        # END OF FUNCTION EXECUTION  #######################
    return result * 2
    # return None


result2 = func_with_return(7)
print(result2)


#

def func_with_return2(x):
    result = False
    if x ** 2 <= 100:
        result = True
    return result


#
#
# print(func_with_return2(10))
# print('-' * 40)
#
#
# return as ternar
def get_max_two(a, b):
    return a if a >= b else b


x, y = 18, 15
print(get_max_two(x, y))

# execution order
x, y, z = 12, 5, 14
print(get_max_two(x, get_max_two(y, z)))


def get_max_three(a, b, c):
    return get_max_two(a, get_max_two(b, c))


print(get_max_three(12, 5, 14))

print('=' * 40)


#

def even(x):
    return x % 2 == 0  # x%2  -> bool(1) -> True   bool(0) ->False


print([itm for itm in range(0, 21) if even(itm)])
print([itm for itm in range(0, 21) if (lambda x: x % 2 == 0)(itm)])
