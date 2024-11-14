# algorithm complexity
# In computer science, big O notation is used to classify
# algorithms according to how their run time or space requirements grow as the input size grows.


# 1. Constant Time (O(1)):

def print_first_element(arr):
    # Print the first element in the array
    print(arr[0])


# Time complexity: O(1)
# data 10 -> operations 1
# data 10 000 - > operations 1
#
#######################################################
# 2. Linear Time (O(n)):
# #     0 1 2
# l1 = [1,2,3]
# l1 = [1,2,3,5,6 ...10000]

def find_element(arr, x):
    # Find the index of element x in the array
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


#
# # Time complexity: O(n)
# # data 10 -> operations 10
# # data 10 000 - > operations 10 000
#
# 3. Quadratic Time (O(n^2)):
def print_pairs(arr):
    # Print all pairs of elements in the array
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i], arr[j])


# Time complexity: O(n^2)
# data 10 -> operations 100
# data 10 000 - > operations 100 000 000

# for complexity O(n^3)
# data 10 000 - > operations 1 trillion


# 4. Logarithmic Time (O(log n)):
# 2
# 0 1 2 3 4 5 6 7 8 9 10
# 0 1 2   3 4
# 0 1 2
# 2
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# Time complexity: O(log n)
# data 100 -> operations 7
# data 10 000 - > operations 14


# 5. Exponential Time (O(2^n)):
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Time complexity: O(2^n)

# data 10 -> operations 1024
# data 20 -> operations 1 048 576

# https://miro.medium.com/v2/resize:fit:1400/1*5VctXSES5PrSk-5lPb_CCg.jpeg


# O(n) + O(n) = O(2n)
# just imagine that n = ∞
# O(2n) -> O(n)

# O(n+n^2) -> O(n^2)
# O(n+log(n) -> O(n)
# O(60*2^n + 10*n^100) -> O(2^n + n^100) -> O(2^n)

n = 100
for i in range(n):
    for j in range(n):
        for k in range(100000):
            print('smth')

# just imagine that n = ∞
# O(n*n*100000) -> O(n^2)


n = 4
for i in range(n):
    for j in range(i, n):
        print(i, j)
# 4 -> 3 -> 2 -> 1

# V V V V
#   V V V
#     V V
#       V

# O(n^2/2) -> O(1/2*n^2) -> O(n^2)
