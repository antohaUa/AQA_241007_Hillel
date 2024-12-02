import math

print(math.pi)

# Importing the math module and renaming it to 'm'
import math as m

# Now we can use functions from the math module by referring to them through 'm'
print(m.sqrt(25))  # Output: 5.0

# # This is equivalent to importing math without renaming and using the full module name
import math
print(math.sqrt(25))
