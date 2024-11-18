import csv

stars = [
    ["Star Name", "Constellation", "Distance (light-years)"],
    ["Sirius", "Canis Major", 8.6],
    ["Betelgeuse", "Orion", 642.5],
    ["Proxima Centauri", "Centaurus", 4.24]
]

with open("stars_custom_delimiter.csv", mode="w", newline="") as file:
    writer = csv.writer(file, delimiter=";", quotechar="'", quoting=csv.QUOTE_ALL)
    writer.writerows(stars)
