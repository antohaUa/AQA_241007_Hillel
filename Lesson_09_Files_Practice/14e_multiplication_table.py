# Given 0 < number (integer) <= 11
# You need to print multiplication table based on this number
#
# Example: num=5
# Output:
#  1   2   3   4   5
#  2   4   6   8  10
#  3   6   9  12  15
#  4   8  12  16  20
#  5  10  15  20  25

# for loop
# double for loop
# range
# center f-string

# 5 -> 2
# 10 -> 3

def multiplication_table(num):
    space = len(str(num*num))
    result = []
    for idx in range(1, num+1):
        line_str = ' '.join([f'{i*idx:>{space}}' for i in range(1, num+1)])
        result.append(line_str)
    return result


print(*multiplication_table(num=31), sep='\n')
