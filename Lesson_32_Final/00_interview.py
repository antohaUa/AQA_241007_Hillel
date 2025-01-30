# t1 = (1, 2, 3, [5,6])  # immutable

# l1 = [1, 2, 3]  # mutable
#
# d1 = {1: 1, t1: 5}
# print(d1)

# list comprehension
# 30-100   N/6 rest == 1  skipped

# lc1 = [el for list in range 30-100 if el/6 !=1]

numbers = [n for n in range(30, 101) if n % 6 != 1]
print(numbers)

l1 = [1, 2, 3]
l2 = ['a', 'b', 'c']

new_dic = {k: v for k, v in zip(l1, l2)}
dict_list = dict(zip(l1, l2))

print(new_dic)
print(dict_list)


class A:
    TT = 15

    def __init__(self, a):
        # print(id(self))
        self.a = a

    def add(self, b=10):
        return self.a + b

    @classmethod
    def some_class_method(cls):
        print(id(cls))
        return cls.TT * 5

    @staticmethod
    def some_call():
        return 40


print(id(A))
instance = A(5)
# print(id(instance))
print(instance.a)
print(instance.some_call())
print(instance.some_class_method())


