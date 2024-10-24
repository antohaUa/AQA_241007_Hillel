# 1  comparison
print(('1', '+', '10') > ('1', '*', '10'))

import sys

p_ver = sys.version_info
print(p_ver)
# (3,8,0)
print(p_ver > (3, 7, 0))


# 2  max occurrence
l_marks = [3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 2, 1, 1]
print(max(l_marks))
print(max(l_marks, key=l_marks.count))

# 3  list vs tuple size
data_list = [2, 3, "Boson", "Higgs", 1.56e-22]
data_tuple = (2, 3, "Boson", "Higgs", 1.56e-22)

print(f'List: {data_list.__sizeof__()} bytes')
print(f'Tuple: {data_tuple.__sizeof__()} bytes')

# 4 unpack
l1 = list(range(1, 100))
print(l1)
print(*l1, sep='\n')
