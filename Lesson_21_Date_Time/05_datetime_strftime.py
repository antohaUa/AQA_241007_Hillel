from datetime import datetime

# Get current local time
local_time = datetime.now()
print(type(local_time))
print(repr(local_time))
print(local_time)
local_time_formatted = local_time.strftime("%Y-%m-%d %H:%M:%S")
print("Local Time with datetime:", local_time_formatted)

# Get current UTC time
utc_time = datetime.utcnow()
utc_time_formatted = utc_time.strftime("%Y-%m-%d %H:%M:%S")
print("UTC Time with datetime:", utc_time_formatted)