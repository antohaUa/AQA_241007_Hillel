# common case
CONST = 15


def my_func2():
    CONST = 5
    print(CONST)


my_func2()
print(CONST)
#
# global
# const = 15
#
# def my_func3():
#     global const
#     const = 7  # here we use const from upper level
#     print(const)
#
#
# my_func3()
# print(const)

# nonlocal
x = 0


def outer():
    # global x
    # nonlocal x   -- > error
    x = 1

    def inner():
        # global x
        nonlocal x
        x = 2  # x from outer scope
        print(f'Inner: {x}')

    inner()
    print(f'Outer: {x}')


print(f'Global: {x}')
outer()
print(f'Global: {x}')
