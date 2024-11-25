class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        """Returns a human-readable string representation of the Car object."""
        return f"{self.make} {self.model} ({self.year})"

    def __repr__(self):
        """Returns a string representation of the Car object that can be used to recreate the object."""
        return f"{self.__class__.__name__}('{self.make}', '{self.model}', {self.year})"


# Create an instance of the Car class
my_car = Car("Toyota", "Camry", 2021)

print(my_car)
print(str(my_car))
print(repr(my_car))
print(my_car.__str__())
print(my_car.__repr__())


#
# # Print the human-readable string representation of the Car object
# print(my_car) # Output: Toyota Camry (2021)
#
# # Print the string representation of the Car object that can be used to recreate the object
# print(repr(my_car))  # Output: Car('Toyota', 'Camry', 2021)
