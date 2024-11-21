class Car:
    max_speed = 200
    color = 'green'
    wheels = 4


print(Car.color)  # green
print(getattr(Car, 'color', 'black'))

setattr(Car, 'max_speed', 500)  # Car.max_speed = 500
print(Car.__dict__)

setattr(Car, 'wheels', 4)
print(Car.__dict__)

delattr(Car, 'wheels')
print(Car.__dict__)

my_car = Car()
my_car.max_speed = 100
setattr(my_car, 'max_speed', 150)
print(my_car.__dict__)
print(my_car.color)
print(my_car.max_speed)

# print(hasattr(my_car, 'wheels'))
# print(Car.__dict__)



