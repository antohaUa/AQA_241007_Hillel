import csv

with open("stars_with_headers.csv", mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
#
#
stars = [
    {"Star Name": "Sirius", "Constellation": "Canis Major", "Distance (light-years)": 8.6},
    {"Star Name": "Betelgeuse", "Constellation": "Orion", "Distance (light-years)": 642.5},
    {"Star Name": "Proxima Centauri", "Constellation": "Centaurus", "Distance (light-years)": 4.24}
]

with open("stars_dict_output.csv", mode="w", newline="") as file:
    fieldnames = ["Star Name", "Constellation", "Distance (light-years)"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()  # Write the header row
    writer.writerows(stars)

new_stars = [
    ["Vega", "Lyra", 25.04],
    ["Polaris", "Ursa Minor", 323]
]

with open("stars_output.csv", mode="a", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(new_stars)