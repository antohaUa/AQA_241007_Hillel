# Parent Class
class Animal:
    """
    The Animal class represents a generic animal.
    This class serves as the parent class for specific types of animals.
    """

    def __init__(self, species, age):
        """
        Initializes an instance of the Animal class.
        :param species: A string representing the species of the animal.
        :param age: An integer representing the age of the animal.
        """
        print('We have started')
        self.species = species
        self.age = age

    def eat(self):
        """
        Simulates the animal's eating behavior.
        """
        # print('animal method:')
        print(f"The {self.species} is eating.")

    def sleep(self):
        """
        Simulates the animal's sleeping behavior.
        """
        print(f"The {self.species} is sleeping.")

    def sound(self):
        """
        Simulates the animal's sound.
        """
        print("The animal makes a sound.")


# Child Class
class Dog(Animal):
    """
    The Dog class represents a specific type of animal - a dog.
    This class inherits from the Animal class and adds dog-specific behavior.
    """

    def __init__(self, species, age, breed):
        """
        Initializes an instance of the Dog class.
        :param species: A string representing the species of the dog.
        :param age: An integer representing the age of the dog.
        :param breed: A string representing the breed of the dog.
        """
        # super() -> same as super(__class__, <first argument>)
        # super(Dog, self).__init__(species, age)
        super().__init__(species, age)  # Animal.__init__(species, age)
        print(self.__dict__)
        self.breed = breed

    def sound(self):
        """
        Overrides the sound method from the parent class.
        Simulates the dog's barking sound.
        """
        print(f"The {self.breed} dog is barking.")

    # def fetch(self):
    #     """
    #     Simulates the dog's fetching behavior.
    #     """
    #     print("The dog is fetching.")


class Cat(Animal):
    def __init__(self, species, age):
        """
        Initializes an instance of the Cat class.
        :param species: A string representing the species of the dog.
        :param age: An integer representing the age of the dog.
        """
        super().__init__(species, age)

    # def sleep(self):
    #     """
    #     Simulates the animal's sleeping behavior.
    #     """
    #     print(f"The {self.species} is sleeping well.")


# Creating instances
# animal = Animal("Generic", 2)
dog = Dog("Dog", 3, "Labrador")
cat = Cat('Barsik', 10)

# Calling methods
# animal.eat()  # Output: The Generic is eating.
# dog.eat()  # Output: The Dog is eating.
# cat.eat()

# animal.sound()  # Output: The animal makes a sound.
dog.sound()  # Output: The Labrador dog is barking.
cat.sound()

dog.eat()  # Output: The Dog is eating.
cat.eat()
#
# dog.fetch()  # Output: The dog is fetching.
# animal.fetch()  # AttributeError: 'Animal' object has no attribute 'fetch'
