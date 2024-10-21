str_list = ["apple", "appke", "banana", "banama", "cherry",
            "dog", "shadow", "birthday", "coffee", "dolphin",
            "elephant", "fireplace", "guitar", "history", "internet",
            "jacket", "kangaroo", "lighthouse", "mountain", "napkin", "ocean", "piano"]

# v2 = str_list.sort()

str_list.sort(reverse=True)
# print(v2)
print(str_list)


# key function
def key_function(x):
    return x[1]


str_list.sort(key=key_function)     # sort by second character
print(str_list)
str_list.sort(key=lambda s: s[1])   # the same but with lambda function
print(str_list)

str_list.sort(key=lambda x: len(x), reverse=True)
print(str_list)

# sorted
str_list2 = ["apple", "Appke", "banana", 'banama', "cherry", "dog", "shadow", "birthday",
             "coffee", "dolphin", "elephant", "fireplace",
             "guitar", "history", "internet", "jacket", "kangaroo",
             "lighthouse", "mountain", "napkin", "ocean", "piano"]
new_sorted_list = sorted(str_list2, key=lambda x: len(x), reverse=False)
print(new_sorted_list)
print(str_list2)


# columns sorting
three_column_list = [
    ("blue", "green", "yellow"),
    ("apple", "banana", "orange"),
    ("dog", "cat", "hamster"),
    ("apple", "winter", "fall"),
    ("book", "pen", "paper"),
    ("car", "bus", "bike"),
    ("apple", "zigzag", "fall"),
    ("sunny", "cloudy", "rainy"),
    ("happy", "sad", "angry"),
    ("mountain", "beach", "lake"),
    ("football", "basketball", "volleyball"),
    ("coffee", "tea", "milk"),
    ("lemon", "lime", "grapefruit"),
    ("jacket", "coat", "sweater"),
    ("movie", "music", "book"),
    ("work", "play", "rest"),
    ("pizza", "burger", "hotdog"),
    ("pencil", "eraser", "sharpener"),
    ("ocean", "river", "stream"),
    ("phone", "laptop", "tablet"),
    ("shirt", "pants", "shoes")
]
three_column_list.sort(key=lambda x: x[0][0] + x[2][0])
print(*three_column_list, sep='\n')


# better to do columns sorting via itemgetter
from operator import itemgetter, attrgetter, methodcaller

three_column_list.sort(key=itemgetter(0, 2))

print(*three_column_list, sep='\n')

# flat list
# https://docs.python.org/3/library/itertools.html
import itertools

data = [[1, 2, 3], [4, 5, 6]]
print(list(itertools.chain.from_iterable(data)))
# [1, 2, 3, 4, 5, 6]


# flat list option #2 (not trivial solution)
l1 = [[1, 2, 3], [4, 5], [6], [7, 8, 9, 0]]
print(sum(l1, []))
