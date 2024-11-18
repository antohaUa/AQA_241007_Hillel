from pathlib import Path

# Create a path object for a file
file_path = Path("example.txt")

# Writing to a file
file_path.write_text("Hello, this is a test file!")

# Reading from the file
content = file_path.read_text()
print(f"File content: {content}")
