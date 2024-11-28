from abc import ABC, abstractmethod, abstractproperty


# Abstract class
class Star(ABC):
    @abstractmethod
    def get_type(self):
        """Abstract method to be implemented by subclasses"""
        pass

    def description(self):
        """Concrete method available to all subclasses"""
        return "This is a celestial star."


# Concrete subclass
class RedDwarf(Star):
    def get_type(self):
        return "Red Dwarf: A small and cool star."


# Concrete subclass
class Supernova(Star):
    def get_type(self):
        return "Supernova: An exploding star at the end of its life cycle."


# Using the classes
red_dwarf = RedDwarf()
print(red_dwarf.description())  # Output: This is a celestial star.
print(red_dwarf.get_type())  # Output: Red Dwarf: A small and cool star.

supernova = Supernova()
print(supernova.description())  # Output: This is a celestial star.
print(supernova.get_type())  # Output: Supernova: An exploding star at the end of its life cycle.

# Attempting to instantiate an abstract class will raise an error
star = Star()  # TypeError: Can't instantiate abstract class Star with abstract method get_type
