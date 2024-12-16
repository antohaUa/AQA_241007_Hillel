# https://docs.python.org/uk/3/library/time.html#time.strftime
import time

# Get current time as local time (system time zone)
local_time = time.localtime()
print(local_time)
local_time_formatted = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
print("Local Time:", local_time_formatted)

# Get current time as UTC time (Greenwich Mean Time)
utc_time = time.gmtime()
utc_time_formatted = time.strftime("%Y-%m-%d %H:%M:%S", utc_time)
print("UTC Time:", utc_time_formatted)

