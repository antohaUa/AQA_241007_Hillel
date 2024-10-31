a = 3

print(isinstance(a, int))

b = True
print(isinstance(b, bool))
print(isinstance(b, int))    # INT -> bool

print(type(b) == bool)
print(type(b) == int)   # strict verification
