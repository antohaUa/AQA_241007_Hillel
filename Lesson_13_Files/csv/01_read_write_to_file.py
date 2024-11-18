# https://docs.python.org/3/library/csv.html

import csv

with open("stars.csv", mode="r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        # print(row[-1])


stars = [
    ["Star Name", "Constellation", "Distance (light-years)"],
    ["Sirius", "Canis Major", 8.6],
    ["Betelgeuse", "Orion", 642.5],
    ["Proxima Centauri", "Centaurus", 4.24]
]

with open("stars_output.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(stars)