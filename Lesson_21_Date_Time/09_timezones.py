# pip install pytz ( python3.9 zonesinfo)
# https://docs.python.org/3/library/zoneinfo.html
from datetime import datetime
import pytz

# Create a datetime object for the current time in UTC
utc_time = datetime.now(pytz.utc)
print("Current UTC Time:", utc_time)

# Convert the UTC time to a different time zone (e.g., New York)
new_york_time = utc_time.astimezone(pytz.timezone("America/New_York"))
print("New York Time:", new_york_time)

# Convert the UTC time to another time zone (e.g., Tokyo)
tokyo_time = utc_time.astimezone(pytz.timezone("Asia/Tokyo"))
print("Tokyo Time:", tokyo_time)

# ============================================================================

# Create a naive datetime object (no timezone info)
naive_time = datetime(2024, 12, 15, 10, 30, 0)
print("Naive Time:", naive_time)

# Localize the naive time to UTC
utc_time = pytz.utc.localize(naive_time)
print("Localized UTC Time:", utc_time)

# Convert the UTC time to another time zone
london_time = utc_time.astimezone(pytz.timezone("Asia/Tokyo"))
print("Tokyo Time:", london_time)

# ============================================================================

# Get the current time in UTC
utc_time = datetime.now(pytz.utc)
print("Current UTC Time:", utc_time)

# Convert to various time zones
for zone in ["America/Los_Angeles", "Europe/London", "Asia/Tokyo"]:
    local_time = utc_time.astimezone(pytz.timezone(zone))
    print(f"Current time in {zone}:", local_time.strftime("%Y-%m-%d %H:%M:%S"))
