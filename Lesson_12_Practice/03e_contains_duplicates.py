# Given an integer array nums, return true if any value appears
# at least twice in the array, and return false if every element is distinct.
# Example 1:
#
# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
#
# Input: nums = [1,2,3,4]
# Output: false

# Example 3:
#
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
###############################

# len + set
# nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

nums = [1, 2, 3, 4]


def check_duplicates(l1):
    return not len(l1) == len(set(l1))
    # set1 = set(l1)
    # if len(l1) == len(set1):
    #     return False


print(check_duplicates(nums))
