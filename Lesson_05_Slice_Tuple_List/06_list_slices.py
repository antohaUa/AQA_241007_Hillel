#                                -2  -1
#     0  1  2  3  4   5   6   7   8   9
l1 = [1, 2, 5, 8, 10, 17, 24, 25, 78, 101]
print(id(l1))
print(l1[0])
print(l1[1])
l2 = l1[2:5]
print(id(l2))
print(l2)
ls1 = l1[2:9:2]  # start: stop: step
print(ls1)
print(id(ls1))
sl3 = l1[:4]
print(sl3)
sl4 = l1[6:]
print(sl4)
sl5 = l1[6:-1]  # start:stop:step
print(sl5)
l2 = l1[:]
print(id(l2))


ls1 = l1[1:12:2]
print(ls1)
ls2 = l1[1:12:2][::-1]  # start:stop:step
print(ls2)
print(l1)
del l1[1:3]
print(l1)