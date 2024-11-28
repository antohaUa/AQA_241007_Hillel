class Vehicle:
    def __init__(self, wheels, max_speed, passengers):
        self.__wheels = wheels
        self.max_speed = max_speed
        self.passengers = passengers

    def __str__(self):
        return f'==[{self.__class__.__name__}]=='

    def ride(self):
        print(f'{str(self)} is riding')

    @property
    def wheels(self):
        return self.__wheels

    @wheels.setter
    def wheels(self, num):
        self.__wheels = num


class Bike(Vehicle):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def ride_one_wheel(self):
        print('OK we ride on one wheel')

    def beep(self):
        print('Tata')


class Car(Vehicle):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def beep(self):
        print('Beep-beep')


class CurrentVehicle:

    def __init__(self, vehicle_object):
        self.vehicle_object = vehicle_object

    def sound(self):
        return self.vehicle_object.beep()


bike = Bike(wheels=2, max_speed=200, passengers=2)
bike.ride_one_wheel()
bike.ride()

car = Car(wheels=4, max_speed=300, passengers=7)
car.ride()
car.wheels = 6
print(car.wheels)

# polymorphysm
curr_vehicle = CurrentVehicle(car)
curr_vehicle.sound()
curr_vehicle.vehicle_object = bike
curr_vehicle.sound()
