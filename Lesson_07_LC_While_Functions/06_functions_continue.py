# functions as objects inside other structures
def func1():
    print(1)


def func2():
    print(2)


def default():
    print('default')
    return  # return None


functions = {0: func1, 1: func2}


def choice_func2(choice=0):
    return functions.get(choice, default)()


choice_func2(0)
choice_func2(1)
choice_func2(100)
