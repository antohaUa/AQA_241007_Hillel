# https://docs.python.org/3/reference/compound_stmts.html#while

counter = 0
#        True
while counter < 10:
    counter += 1
    if counter == 5:
        # continue
        break
    print(counter)
else:
    print('Done')

a = 0
while True:
    a += 1
    print('. ', end=' ')
    if a == 5:
        break

print()
#
# 1-30   3, 6,9,12,15,18
n = 0
while n < 30:
    n += 3
    print(n)

n = 0
while n < 30:
    n += 1
    if n % 3 == 0:
        print(n)
# #
# # condition = 11 > 10 and 2 > 1 and 2 > 1 and 2 > 1 and 2 > 1
# # lc1 = [el for el in range(1, 31) if el % 3 == 0 and condition]
# # print(lc1)
