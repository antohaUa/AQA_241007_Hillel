# https://peps.python.org/pep-0590/

class Test:
    @staticmethod
    def func1():
        print('1234')

    X = func1()


print(Test.X)
