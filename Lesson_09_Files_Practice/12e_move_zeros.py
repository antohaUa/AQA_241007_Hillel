# Given an integer array nums, move all 0's to the end of it while maintaining
# the relative order of the non-zero elements.

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
l1 = [0, 1, 0, 3, 12]


# count zeros + add right
# filter non 0 values

def move_zeros(l_nums):
    l2 = [i for i in l_nums if i != 0]
    z_count = l_nums.count(0)
    l2.extend([0] * z_count)
    return l2


def move_zeros2(l_nums):
    l2 = [i for i in l_nums if i != 0]
    l2.extend([0] * l_nums.count(0))
    return l2


print(move_zeros2(l1))
