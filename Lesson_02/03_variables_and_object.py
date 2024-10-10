# https://miro.medium.com/v2/resize:fit:4800/format:webp/1*bfKd7I03UAxi_bfwW5SAjQ.png
# https://tenthousandmeters.com/
# https://medium.com/@sergioli/how-python-objects-are-implemented-in-c-2f36ff8fb371
# """
#     Python variables are names mapped to values.
#     Values of names are references to Python objects.
# """
# sudo gdb --pid <PID>
# dump memory /tmp/mem_file 0x7fe4d46f90b0 0x7fe4d46f90b0
# https://github.com/python/cpython/blob/main/Include/object.h

v1 = 'Some Text'
v2 = 1234
v3 = object
print(v1.__sizeof__())  # get object size in bytes
print(v2.__sizeof__())
print(v1.__class__.__bases__)  # get base class of variable. All points to object
print(v2.__class__.__bases__)  # get base class of variable. All points to object
print(v3.__class__.__bases__)  # get base class of variable. All points to object

v11 = v1  # now we have two references
print(id(v11))  # the same ref to memory as v1
print(id(v1))  # the same ref to memory as v11
del v1  # string object in memory now has one reference
del v11  # no references - garbage collector starts

a = 5
b = 6

print(a)
# print('=' * 50)
# v10 = 'text1'
# v11 = v10
# print(id(v10))
# print(id(v11))
# print('-' * 10)
# v11 = 'text2'    # reference to new object and thus id(v10) now != id(v11)
# print(id(v10))
# print(id(v11))
