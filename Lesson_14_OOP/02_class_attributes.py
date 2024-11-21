# class Point(object):
#     pass
#
#
# d1 = {Point: 1}    # classes are hashable and could be used as dict keys
# print(d1)
#
#
# # attributes
# # variables visibility area
# class Point:
#     x = 5
#     print(x)
#     y = 10
#
#
# print(Point.x)
# Point.x = 3
# print(Point.x)
# # print(dir(Point))
# print(Point.__dict__)
# print(Point.__class__.__bases__)
#
# # class instance
# class Point:
#     x = 5
#     y = 10
#
# #
# p1 = Point()
# p2 = Point()
# # # p1()
# # print(id(p1))
# # print(id(p2))
# # print(type(p1))
# #
# print(p1.__dict__)
# print(p2.__dict__)
# print(Point.__dict__)
# # # own visibility area   (outer/inner functions analog)
# # p1.x = 11
# # p1.y = 15
# print(p1.__dict__)
# Point.x = 100
# p1.x = 200
# print(Point.x)
# print(p1.x)
#

class Point:
    x = 5
    y = 10

# attributes operations
# Point.z = 1000
# print(Point.z)
# print(Point.__dict__)
# # Point.color = 'red'
# # print(Point.__dict__)
# setattr(Point, 'color', 'green')
# print(Point.__dict__)
# Point.color = 'green'
# print(Point.__dict__)
# print(Point.color)
# # #
# # # possible Attribute error
# print(Point.non_existing)
# #
# d1 = {'a':1}
# #'b'
# b = d1.get('b', 1000000)
# print(b)
# print(Point.non_existing)  # Attribute Error
print(getattr(Point, 'non_existing', 'Default')) # Safety getattr
# # # #print(Point.non_existing)
# print(Point.__dict__)
# del Point.color
# print('-'*50)
# print(Point.__dict__)

if hasattr(Point, 'color'):
    print('Color should be deleted now')
    delattr(Point, 'color')
else:
    print("attr not exists")

# hasattr()
# getattr()   ->   # Point.color
# setattr()   ->   # Point.color = 'green'
# delattr()   ->   # del Point.color
#
#
