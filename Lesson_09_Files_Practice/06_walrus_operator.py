# :=
text = 'Some string to split'

print(text.split())
print(''.join(text.split()))
print(len(''.join(text.split())) / len(text.split()))

operations = {
    'words': text.split(),
    'letters_count': len(''.join(text.split())),
    'avg_letters_per_word': len(''.join(text.split())) / len(text.split())
}
print(operations)

operations2 = {
    'words': (words := text.split()),
    'letters_count': (l_count := len(''.join(words))),
    'avg_letters_per_word': l_count / len(words)
}
#

print(operations2)


def func(x):
    return x ** 2


lc = [func(itm) for itm in range(11) if func(itm) < 100]
lc2 = [res for itm in range(11) if (res := func(itm)) < 100]
# print(res)
print(lc)
print(lc2)

# regexp
import re

s1 = 'hello World'
if result := re.match(r'^[hH]ello [wW]orld', s1):
    print(bool(result))
