# def func1(a, b=12312, **kwargs):
#     print(a)
#     print(b)
#     print(kwargs)
#
#
# func1(10, b=14, c=15, y='3243')


class A:
    def __init__(self, a, **kwargs):
        self.a = a


class B(A):
    def __init__(self, a, b=123, **kwargs):
        self.b = b
        super().__init__(a, **kwargs)


class C(A):
    def __init__(self, a, c=321, **kwargs):
        self.c = c
        super().__init__(a, **kwargs)


class D(B, C):
    def __init__(self, a, b, c, d):
        self.d = d
        super().__init__(a, b=b, c=c)


#      a  b  c   d
d1 = D(4, 5, 6, 7)
print(d1.a)
print(d1.b)
print(d1.c)
print(d1.d)
print(D.__mro__)
