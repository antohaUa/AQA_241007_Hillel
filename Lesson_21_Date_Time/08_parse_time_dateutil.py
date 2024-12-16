# pip install python-dateutil
# https://github.com/dateutil/dateutil
from dateutil import parser

# ISO 8601 format: YYYY-MM-DDTHH:MM:SS
date_string = "2021-12-15T10:30:45"
parsed_date = parser.parse(date_string)
print("Parsed Date:", parsed_date)

# ISO 8601 format with timezone offset: YYYY-MM-DDTHH:MM:SS±HH:MM
date_string_with_tz = "2024-08-31T01:30:45+03:00"
parsed_date_with_tz = parser.parse(date_string_with_tz)
print("Parsed Date with Timezone:", parsed_date_with_tz)

# Date with day of the week and time: Day, DD Mon YYYY HH:MM:SS
date_string_with_day = "Sun, 01 Dec 2024 07:22:49"
parsed_day_date = parser.parse(date_string_with_day)
print("Parsed Date with Day:", parsed_day_date)

# Date with abbreviated month: DD Mon YYYY
date_string_with_abbr_month = "01 Dec 2024"
parsed_date_abbr_month = parser.parse(date_string_with_abbr_month)
print("Parsed Date with Abbreviated Month:", parsed_date_abbr_month)

# Time with hour and minute (no year): HH:MM AM/PM
time_string = "03:35 PM"
parsed_time = parser.parse(time_string)
print("Parsed Time:", parsed_time)

# Custom date format: MM/DD/YYYY
custom_date_string = "12/15/2024"
parsed_custom_date = parser.parse(custom_date_string)
print("Parsed Custom Date:", parsed_custom_date)

# Date with weekday name and timezone: Day, DD Mon YYYY HH:MM:SS ±HHMM
date_with_weekday_and_tz = "Sun, 15 Dec 2024 10:30:45 +0300"
parsed_date_with_weekday_tz = parser.parse(date_with_weekday_and_tz)
print("Parsed Date with Weekday and Timezone:", parsed_date_with_weekday_tz)

# Parsing natural language date (relative date)
date_string_natural = "next Tuesday"
parsed_natural_date = parser.parse(date_string_natural, fuzzy=True)
print("Parsed Natural Date:", parsed_natural_date)