import time

# Define a tuple representing a time
time_tuple = (2024, 12, 31, 11, 30, 0, 0, 0, -1)
# (year, month, day, hour, minute, second, weekday, yearday, isdst)
# Weekday (0-6, where 0 is Monday)
# Year day (1-366; -1 means calculate automatically)
# Is DST (Daylight Saving Time flag: -1 for auto, 0 for no, 1 for yes)

# Convert tuple to a Unix timestamp
timestamp = time.mktime(time_tuple)
print("Timestamp:", timestamp)

# Convert timestamp back to a readable time
readable_time = time.ctime(timestamp)
print("Readable Time:", readable_time)

