from pathlib import Path

# # Create a path object for a file
# file_path = Path("some_file.txt")
#
# # Check if the file exists
# if file_path.exists():
#     print(f"The file {file_path} exists.")
# else:
#     print(f"The file {file_path} does not exist.")

# Create a path object for a file
file_path = Path("/home/user/documents/file.txt")

# Get the file name
print(f"File name: {file_path.name}")

# Get the file extension
print(f"File extension: {file_path.suffix}")

# Get the parent directory
print(f"Parent directory: {file_path.parent}")