# Given an integer num, repeatedly add all its digits until
# the result has only one digit, and return it.
# Input: num = 38
# Output: 2
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2
# Since 2 has only one digit, return it.

number = 1922  # -> 1922 ->  14 - > 5


# int -> str
# split + int -
# list comprehension

# len == 1
# while ( but not for)

def magic_num(num):
    value = num
    while len(str(value)) > 1:
        sum1 = sum([int(itm) for itm in str(value)])
        value = sum1
    return value


def magic_num2(num):
    value = num
    while value >= 10:
        value = sum([int(itm) for itm in str(value)])
    return value


print(magic_num2(387098789797))
print(magic_num2(1922))
