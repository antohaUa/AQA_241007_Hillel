# H e l l o   W o r l d  !
# 0 1 2 3 4 5 6 7 8 9 10 11

s1 = 'Hello world!'

# In [31]: s1[1:11]
# Out[31]: 'ello world'
#
# In [32]: s1[0:11]
# Out[32]: 'Hello world'
#
# In [33]: s1[0:12]
# Out[33]: 'Hello world!'
#
# In [34]: s1[0:12:2]
# Out[34]: 'Hlowrd'
#
# In [35]: s1[:12:2]
# Out[35]: 'Hlowrd'
#
# In [36]: s1[::2]
# Out[36]: 'Hlowrd'
#
# In [37]: s1[5:]
# Out[37]: ' world!'


print(s1[::-1])

s1 = 'Some String with Greetings!'
s2 = 'Some Text with Spam!'
target_slice = slice(4, None, None)
print(s1[target_slice])
print(s2[target_slice])

# Example:
# take last 5 characters from string
s1 = 'String with Greetings!'
print(s1[22-5:])
print(s1[len(s1)-5:])
print(s1[-5:])
# All prints will give us -> 'ings!'


