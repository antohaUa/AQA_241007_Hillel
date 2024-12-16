from datetime import datetime

# A string representing a date and time
time_string = "2024-12-31 10:30:45"

# Define the format of the time string
time_format = "%Y-%m-%d %H:%M:%S"

# Parse the string into a datetime object
parsed_datetime = datetime.strptime(time_string, time_format)

# Print the parsed datetime object
print("Parsed Datetime:", parsed_datetime)

# You can also extract specific parts of the datetime object
print("Year:", parsed_datetime.year)
print("Month:", parsed_datetime.month)
print("Day:", parsed_datetime.day)
print("Hour:", parsed_datetime.hour)
print("Minute:", parsed_datetime.minute)
print("Second:", parsed_datetime.second)