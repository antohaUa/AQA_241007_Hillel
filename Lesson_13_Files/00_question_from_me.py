l1 = [1, 2, 3, 4, 5, 6]

for i in l1:
    print(f'Befor pop {i=} {l1=}')
    print(f'Current pop value = {l1.pop()}')
    print(f'After pop {i=} {l1=}')
print('=' * 50)

l1 = [1, 2, 3, 4, 5, 6]

for i in l1[:]:
    # print(f'Befor pop {i=} {l1=}')
    print(f'Current pop value = {l1.pop()}')
    # print(f'After pop {i=} {l1=}')
print('=' * 50)

l1 = [1, 2, 3, 4, 5, 6]
it1 = iter(l1)
# it1 = l1.__iter__()
print(f'Iterator length = {it1.__length_hint__()}')
print(next(it1))
l1.pop()
print(f'Iterator length = {it1.__length_hint__()}')
print(next(it1))
l1.pop()
print(f'Iterator length = {it1.__length_hint__()}')
print(next(it1))
l1.pop()
print(f'Iterator length = {it1.__length_hint__()}')

print('=' * 50)
