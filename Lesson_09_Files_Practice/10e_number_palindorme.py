# Given an integer x, return true if x is a palindrome , and false otherwise.
# Input: x = 121
# Output: true
x = 13231  #

# true

# x = 1234  # -> false
"""
#  middle ?
#  int -> str +
#  list reverse
#  str slice +
#  compare +

"""


def palindrom_check(num):
    """Check ...."""
    v1 = str(num)
    v2 = v1[::-1]
    return v1 == v2


def palindrom_check2(num):
    return str(num) == str(num)[::-1]


print(palindrom_check2(13231))
print(palindrom_check2(1234))
print(palindrom_check2(121))
