def auth(func):
    def deco(*args, **kwargs):
        return func(*args, **kwargs)

    return deco


class A:

    @auth
    def func1(self):
        print('Func1')

    def func2(self):
        print('Func2')


class_a = A()
class_a.func1()
