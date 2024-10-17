# # string creation with str()

s1 = [1, 2, 3]
print(s1.__str__())
print(s1.__repr__())

b1 = True
b2 = str(b1)

print(type(s1))

s2 = str(s1)
print(type(s2))
print(f'"{s2}"')

print(str(b'\x89\x20\x31\x32\x33', encoding='utf-8', errors='ignore'))
print(str(b'\x89\x20123', encoding='utf-8', errors='ignore'))

print(str(b'\x89\x20\x31\x32\x33', encoding='utf-8'))

# additional examples
print(str(range(10)))
print(str(1))

print('\u00a9')
print('\u1f98')

# module string
import string

print(string.ascii_lowercase)
print(string.ascii_letters)
print(string.digits)
print(string.hexdigits)
print(string.punctuation)
print(string.capwords('hello world'))

str1 = '   Value    '
print(str1.lstrip())
print("What's wrong with ASCII?!?!?*".rstrip("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'"""))
print("What's wrong with ASCII?!?!?*  ".rstrip(f'{string.punctuation}{" "}'))
print("What's wrong with ASCII?!?!?*  ".rstrip(string.punctuation + " "))
