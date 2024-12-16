from datetime import datetime, timedelta

# Define two datetime objects
time1 = datetime(2024, 12, 15, 10, 30, 0)
time2 = datetime(2024, 12, 15, 12, 45, 0)

# Calculate the time difference
time_difference = time2 - time1

# Print the result
print("Time Difference:", time_difference)

# You can extract specific components of the timedelta
print("Days:", time_difference.days)
print("Seconds:", time_difference.seconds)
print("Total seconds:", time_difference.total_seconds())
#
# =================================================================

# Get the current time
current_time = datetime.now()

# Define another datetime (e.g., 2 hours ago)
past_time = current_time.replace(hour=current_time.hour - 2)

# Calculate the time difference
time_difference = current_time - past_time

# Print the result
print("Time Difference:", time_difference)

# =================================================================

now = datetime.now()

# Subtract 5 days from the current date
five_days_ago = now - timedelta(days=5)
print("5 Days Ago:", five_days_ago)

# Add 10 hours to the current date
ten_hours_later = now + timedelta(hours=10)
print("10 Hours Later:", ten_hours_later)

# =================================================================

# Define two datetime objects
start_time = datetime(2024, 12, 11, 10, 0, 0)
end_time = datetime(2024, 12, 31, 14, 39, 24)

# Calculate the time difference
time_difference = end_time - start_time

# Calculate hours, minutes, and seconds from the total seconds
hours = time_difference.total_seconds() // 3600
minutes = (time_difference.total_seconds() % 3600) // 60
seconds = time_difference.total_seconds() % 60

# Print the result
print(f"Time Difference: {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds")
