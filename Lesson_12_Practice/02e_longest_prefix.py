# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string ""
# Input: strs = ["flower","flow","flight"]
# Output: "fl"


# cycle
# find min word
# min
# all
# slice

strs = ["flower", "flow", "flight"]


def prefix(l1):
    min_word = sorted(l1, key=len)[0]
    prf = ''
    for idx, ch in enumerate(min_word):  # f # fl # flo
        if not all(itm.startswith(min_word[:idx+1]) for itm in l1):
            break
        prf = min_word[:idx+1]
    return prf
    #print(min_word[:idx+1])


    # for ch in min_word:
    # for curr_str in l1:
    #     print(curr_str)
    #     curr_str.startswith(min_word[0])

    # print(l2)
    # # for i in l1:
    # #     if len(i)


print(prefix(strs))
