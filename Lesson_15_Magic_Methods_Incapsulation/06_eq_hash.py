class Person:
    def __init__(self, ssn, name):
        self.ssn = ssn
        self.name = name

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.ssn == other.ssn
        return False


# Usage
p1 = Person("123-45-6789", "Frank")
p2 = Person("123-45-6789", "David")

print(p1 == p2)

# Attempting to use in a set
# people = {p1, p2}  # Raises TypeError: unhashable type: 'Person'


###############################################
#
class Person:
    def __init__(self, ssn, name):
        self.ssn = ssn
        self.name = name

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.ssn == other.ssn
        return False

    def __hash__(self):
        return hash(self.ssn)

    def __repr__(self):
        return f'{self.ssn}-{self.name}:{hash(self.ssn)}'


# Usage
p1 = Person("123-45-6789", "Frank")
p2 = Person("123-45-6789", "David")  # Same SSN as p1
p3 = Person("987-65-4321", "Kenny")

print(p1 == p2)  # Output: True
print(p1 == p3)  # Output: False

# Using in a set
people = {p1, p2, p3}
print([itm for itm in people])
