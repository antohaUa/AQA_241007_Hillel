magic_num = 11321  # use readable variables names
CONSTANT = 1
# remember that some names are reserved by python
# get list of available built-in functions
# -----------------------------------------
import builtins

print(*dir(builtins), sep='\n')
# -----------------------------------------
# list keywords
# -----------------------------------------
from keyword import kwlist

print('\n'.join(kwlist))
# -----------------------------------------
# [DOC & help]
# https://docs.python.org/3/library/string.html

v1 = object
print(help(dir))
print(*dir(v1), sep='\n')
print(repr(v1))

# get list of available modules
# -----------------------------------------
help('modules')

loop_counter = 10


# str = '32423'
# print(str(10))  # here will be error cause "str" is reserved word

# to check if string could be used as variable name
variable_name = 's1x2'
print(variable_name.isidentifier())
variable_name = '123_True'
print(variable_name.isidentifier())
