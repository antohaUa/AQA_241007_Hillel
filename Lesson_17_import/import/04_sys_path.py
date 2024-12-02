import lxml

import sys

# Displaying the current search paths
print("Current search paths:")

print(type(sys.path))
# sys.path.append('/tmp')
for path in sys.path:
    print(path)
print('-' * 40)
#
# # sys.path.append('/tmp')
# # or
# # export PYTHONPATH=:/tmp:/new_dir
#
if __name__ == '__main__':
    import tmp_module2

    tmp_module2.tmp_function()
