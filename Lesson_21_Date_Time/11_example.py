"""
2024-12-15 10:00:23 - Thread 1: Event 1 occurred
2024-12-15 10:02:13 - Thread 2: Event 1 occurred
2024-12-15 10:04:03 - Thread 3: Event 1 occurred
2024-12-15 10:05:13 - Thread 1: Event 2 occurred
2024-12-15 10:07:43 - Thread 2: Event 2 occurred
2024-12-15 10:08:23 - Thread 3: Event 2 occurred
2024-12-15 10:10:13 - Thread 1: Event 3 occurred
2024-12-15 10:12:03 - Thread 2: Event 3 occurred
2024-12-15 10:14:23 - Thread 3: Event 3 occurred
"""

import time


# open and parse file
# list : dict iside  Thread: ID , Event: id ,  strptime
# for each thread sort events by id  - > [time_obj1, time_ob2, time_obj3]
# result object for each list -> dict


def parse_log(log_file):
    with open(log_file, 'rt') as l_fh:
        log_file_lines = l_fh.readlines()
        # print(log_file_lines)

    # structure
    parsed_time_list = []
    for itm in log_file_lines:
        time_str = itm.split(' - Thread')[0]
        # Define the format of the time string
        time_format = "%Y-%m-%d %H:%M:%S"

        # Parse the string into a struct_time object
        parsed_time = time.strptime(time_str, time_format)
        human_time = time.strftime("<%H:%M:%S>", parsed_time)
        parsed_time_list.append(human_time)

    print(parsed_time_list)


parse_log('11_example.log')
