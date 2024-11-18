from pathlib import Path

# Specify the directory to search
directory = Path("/tmp")

# Recursively get all .txt files in the directory and subdirectories
txt_files = directory.rglob("*.txt")

# Iterate through the found text files
for file in txt_files:
    # Print the file path
    print(f"File path: {file}")

    # Check if the file exists and is readable
    if file.exists() and file.is_file():
        # Read the first line of the file
        with file.open() as f:
            first_line = f.readline().strip()  # Using readline() to get the first line
            # Print the first line of the file
            print(f"First line of {file.name}: {first_line}\n")
    else:
        print(f"Cannot read {file}")