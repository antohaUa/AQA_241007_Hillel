# ===============================================================
# public
# full access
class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels


v1 = Vehicle(wheels=4)
print(v1.wheels)


# ===============================================================
# protected
# access in current class and child classes

class Vehicle2:
    def __init__(self, wheels):
        self._wheels = wheels


print('-' * 30)
v1 = Vehicle2(wheels=2)
v1._wheels = 6
print(v1._wheels)  # only warning


# ===============================================================
# private  ( setters/getters)
# access only form current class
class Secret3:
    def __init__(self, password):
        self.__password = password


secr = Secret3('sdfsdf')

# print(secr._Secret3__password)   # hack
# print(secr.__password)

class Vehicle3:
    def __init__(self, wheels):
        self.__wheels = wheels
        #self.__year = year

    def get_wheels_num(self):             # getter
        return self.__wheels

    def set_wheels_num(self, wheels):    # setter
        self.__wheels = wheels

    def __prn(self, smth):
        return smth

    def get_prn(self, smth):
        return self.__prn(smth=smth)

v1 = Vehicle3(wheels=5)

# print(v1.__wheels)
# print(v1._Vehicle3__wheels)

print(v1.get_wheels_num())
v1.set_wheels_num(wheels=10)
print(v1.get_wheels_num())
print(v1.get_prn('Hello'))

# setters and getters via @property
class Vehicle4:
    def __init__(self, wheels):
        self.__wheels = wheels

    @property  # doc
    def wheels(self):
        return self.__wheels

    @wheels.setter
    def wheels(self, wheels):
        # additional checks
        self.__wheels = wheels


print('=' * 10)
v4 = Vehicle4(wheels=10)
print(v4.wheels)
v4.wheels = 5  # setter
print(v4.wheels)  # getter


# real protected and private
# pip install accessify
# from accessify import protected, private
# https://github.com/dmytrostriletskyi/accessify