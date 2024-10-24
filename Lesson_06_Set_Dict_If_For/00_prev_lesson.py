# do not commit two and more hometask files in one pull request


"""
sum(iterable, /, start=0)
    Return the sum of a 'start' value (default: 0) plus an iterable of numbers

    When the iterable is empty, return the start value.
    This function is intended specifically for use with numeric values and may
    reject non-numeric types
"""

# flat list option #2 (not trivial solution)
l1 = [[1, 2, 3], [4, 5], [6], [7, 8, 9, 0]]
print(sum(l1, []))

l1 = [1, 2, 5, 8, 10, 17, 24, 25, 78, 101]
ls2 = l1[1:12:2][::-1]  # start:stop:step

[*l2] = l1
