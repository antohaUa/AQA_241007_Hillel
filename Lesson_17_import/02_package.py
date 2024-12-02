# import mypackage
#
# print(mypackage.CONSTANT1)
#
# from mypackage import CONSTANT1
# print(CONSTANT1)

# from mypackage import *
# print(CONSTANT1)
# function1()  # This works
# function2()  # This works

# import mypackage
#
# mypackage.some_func()

# from mypackage.module1 import function1
# function1()

from mypackage import function1
from logger_new import new_logger

function1()
new_logger()
