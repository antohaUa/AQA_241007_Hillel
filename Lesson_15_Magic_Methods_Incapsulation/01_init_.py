class Vehicle:
    wheels = 4
    year = 2023


v1 = Vehicle()
v1.wheels = 2
v1.year = 2021


print(v1.__dict__)
print(Vehicle.wheels)


###### init
class VehicleInit:
    def __init__(self, wheels=4, year=2023, eng_vol=2):
        print('WE are in INIT')
        self.wheels = wheels
        self.year = year
        self.eng_vol = eng_vol
        print(self.__dict__)


motobike = VehicleInit(wheels=2, year=2021, eng_vol=1)
print(motobike.wheels)

big_car = VehicleInit(wheels=6, year=1980, eng_vol=6)
print(big_car.wheels)

v4 = VehicleInit()
print(v4.wheels)
