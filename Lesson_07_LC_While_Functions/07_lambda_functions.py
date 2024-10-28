l1 = ['sdfsdf', 'dfsd', 'z', 'zb']
l1.sort(key=lambda x: len(x), reverse=True)
print(l1)
#
# l1 = [1, 2, 3, 4, 4, 5]
#
# l2 = sorted(l1, key=lambda x: x < 3)
#
# # l1 = [True, False, True]
# # print(sorted(l1))
#
# def name(x):
#     return x < 3
#
# print(l2)
#
# function without name
fn = lambda a, b: a + b
#
# def fn(a,b):
#      return a+b
#
print(fn(7, 8))
#
l2 = [0, 1, 2, lambda: 3, 4, 5]
# def fn2():
#     return 3

print(l2[3])
print(l2[3]())

l3 = [1, 4, -9, 12, 18, 23]


def get_filter(l, filter_func=None):
    if filter_func is None:
        return l
    else:
        return [el for el in l if filter_func(el)]


result = get_filter(l3, lambda x: x % 2 != 0)
result2 = get_filter(l3, lambda x: x < 0)
result3 = get_filter(l3, lambda x: len(str(x)) >= 2)
print(result)
print(result2)
print(result3)
