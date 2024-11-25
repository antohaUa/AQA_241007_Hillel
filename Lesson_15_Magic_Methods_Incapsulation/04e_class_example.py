class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self, increment):
        self.speed += increment

    def brake(self, decrement):
        self.speed -= decrement

    def __str__(self):
        return f"Car({self.make} {self.model} {self.year}) current_speed = {self.speed}"


if __name__ == '__main__':
    print('Something will be printed during import')
    print(__name__)

    print('Script was called directly')
    # Instantiate a Car object
    my_car = Car("Tesla", "Model 3", 2021)

    my_car.accelerate(130)
    print(my_car)

    my_car.brake(100)
    print(my_car)
