from datetime import datetime
import re
log_string = '{ Trade (101, len 36) Queue 0 PriceClass 1 Timestamp 05:45:09 Key TSTFEED0020|7E3E|0400 TradePrice 5 TradeSize 0 }'

pattern = r'Timestamp\s(\d{2}:\d{2}:\d{2})'
# search_obj = re.search(pattern, log_string)
if search_obj := re.search(pattern, log_string):
    timestamp_str = search_obj.group(0)
    print(timestamp_str)
    curr_time = search_obj.group(1)
    time_format = "%H:%M:%S"
    parsed_time = datetime.strptime(curr_time, time_format)
    print(parsed_time)
    #print(search_obj.group(2))
else:
    print('Nothing')






# breakpoint()
# a = 5

# time_format = "%H:%M:%S"
# time_string = '05:45:09'
#
# # Parse the string into a datetime object
# parsed_time = datetime.strptime(time_string, time_format)
# print(parsed_time)