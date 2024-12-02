# Define the module name dynamically
module_name = "math"

# Dynamically import the module using the built-in __import__() function
imported_module = __import__(module_name)

# Now we can use functions from the dynamically imported module
print(imported_module.sqrt(25))  # Output: 5.0

#
# # Importing the importlib module
# # https://docs.python.org/3/library/importlib.html
# import importlib
# import requests
#
# # Define the module name dynamically
# module_name = "math"
#
#
# # Dynamically import the module using importlib.import_module()
# imported_module = importlib.import_module(module_name)
#
# # Now we can use functions from the dynamically imported module
# print(imported_module.sqrt(25))  # Output: 5.0
