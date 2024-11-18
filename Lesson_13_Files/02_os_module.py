# https://docs.python.org/3/library/os.html
import os
#
# # =================================================================================
# # List all files and directories in the current directory
# current_directory = os.getcwd()
# print(f"Files and directories in '{current_directory}':")
# for item in os.listdir(current_directory):
#     print(item)
#
# # =================================================================================
# # Create a new directory
# directory_path = "new_directory"
# if not os.path.exists(directory_path):
#     os.makedirs(directory_path)
#     print(f"Directory '{directory_path}' created successfully.")
# else:
#     print(f"Directory '{directory_path}' already exists.")
#
# # =================================================================================
# # Check if a file exists
# file_path = "some_file.txt"
# if os.path.isfile(file_path):
#     print(f"The file '{file_path}' exists.")
# else:
#     print(f"The file '{file_path}' does not exist.")
# # =================================================================================
# # # Check if a directory exists
# # directory_path = "some_directory"
# # if os.path.isdir(directory_path):
# #     print(f"The directory '{directory_path}' exists.")
# # else:
# #     print(f"The directory '{directory_path}' does not exist.")
# #
# # # =================================================================================
#
#
# # Delete the file
# file_to_delete = "file_to_delete.txt"
# if os.path.exists(file_to_delete):
#     os.remove(file_to_delete)
#     print(f"The file '{file_to_delete}' has been deleted.")
# else:
#     print(f"The file '{file_to_delete}' does not exist.")
#
# # =================================================================================
# # Change the permissions to 755 (rwxr-xr-x)
# # Owner can read, write, and execute; group and others can read and execute.
# file_path = 'example_file.txt'
# try:
#     os.chmod(file_path, 0o755)
#     print(f"Permissions of '{file_path}' changed successfully to 755.")
# except Exception as e:
#     print(f"Error: {e}")

# =================================================================================
# os.path.join
p1 = '/var/log'
p2 = r'data/temp_file.log'
p3 = r'C:\temp'
print(os.path.join(p1, p2))
