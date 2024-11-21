import random


class CustomList(list):
    def __str__(self):
        return ' -> '.join([str(itm) for itm in self])

    def shuffle(self):
        target_list = self.copy()
        random.shuffle(target_list)
        return target_list


l1 = [1, 2, 3, 4]
print(f'String: {l1}')

l2 = CustomList(l1)
print(f'String: {l2}')
l2.append(40)
print(l2)
#
print(l2.shuffle())
print(l2.shuffle())
print(l2.shuffle())

