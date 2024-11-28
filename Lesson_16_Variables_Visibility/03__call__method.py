# make class object callable ( behave as function)
class SomeCounter:
    def __init__(self):
        self.__counter = 0

    def __call__(self, *args, **kwargs):
        print('Here was call')
        start = kwargs.get('start', 1)
        self.__counter += start
        return self.__counter


counter = SomeCounter()
# counter()
# # c()
print(counter())
print(counter())
print(counter())
print(counter())


# call usage for frequently used methods as alias

class SomeCounter2:
    def __init__(self):
        self.__counter = 0

    def hello_world(self, name):
        print(f'{name} Hello World!')

    def __call__(self, *args, **kwargs):
        return self.hello_world(*args, **kwargs)


c2 = SomeCounter2()
c2.hello_world('Bob')
c2('Adam')
c2('Petro')
