class Counter:
    def __init__(self, max_value):
        self.max_value = max_value
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.max_value:
            self.current += 2
            return self.current
        else:
            raise StopIteration


# Using the iterator
counter = Counter(15)
# for number in counter:
#     print(number)

# iter1 = counter.__iter__()
iter2 = iter(counter)
print(next(iter2, 'default'))
print(next(iter2, 'default'))
print(next(iter2, 'default'))
print(next(iter2, 'default'))
print(next(iter2, 'default'))
print(next(iter2, 'default'))
