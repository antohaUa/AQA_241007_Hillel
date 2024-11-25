# super(cls, obj)

# super(OurClass, self) -> super()


class A:
    def __init__(self):
        print("A's __init__ called")
        super().__init__()  # super(A, self).__init__()


class B:
    def __init__(self):
        print("B's __init__ called")
        super().__init__()


class C(A, B):
    def __init__(self):
        print("C's __init__ called")
        super(C, self).__init__()


c = C()
print(C.__mro__)


########################################

class Parent:

    def greet2(self):
        print("Hello greet2 from Parent!")

    def greet(self):
        print("Hello from Parent!")


class Child(Parent):
    def greet(self):
        print("Hello from Child!")
        # super(Child, self).greet()
        super().greet()  # Parent.greet()


ch = Child()
ch.greet()
ch.greet2()
