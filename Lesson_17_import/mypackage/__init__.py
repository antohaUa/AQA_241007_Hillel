# Importing specific items from submodules to include in the package
from .module1 import function1, CONSTANT1
from .module2 import function2


# import time
# time.sleep(5)

def some_func():
    print('Some package FUNCTION')


# Defining what gets imported with 'from mypackage import *'
# __all__ = ['CONSTANT1', 'function1']
__all__ = ['CONSTANT1', 'function1', 'function2']
