# https://docs.python.org/uk/3/library/shutil.html
import shutil

# Copy a file to another location
shutil.copy('example_file.txt', 'backup/example_file.txt')

# Move the file to another location
shutil.move('example_file.txt', 'new_folder/example_file.txt')

# shutil.copy2(): Similar to copy(), but also preserves file metadata.