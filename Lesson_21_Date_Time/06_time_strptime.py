import time

# A string representing a date and time
time_string = "2024-12-31 11:30:45"

# Define the format of the time string
time_format = "%Y-%m-%d %H:%M:%S"

# Parse the string into a struct_time object
parsed_time = time.strptime(time_string, time_format)

# Print the struct_time object
print("Parsed Time (struct_time):", parsed_time)
breakpoint()

# Convert the struct_time to a more readable string format
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", parsed_time)
print("Formatted Time:", formatted_time)