# https://wiki.python.org/moin/YAML
import yaml

with open("stars.yaml", "r") as fh:
    data = yaml.safe_load(fh)
    for star in data:
        print(f"{star['name']} is in {star['constellation']} and is {star['distance']} light-years away.")


stars = [
    {"name": "Sirius", "constellation": "Canis Major", "distance": 8.6},
    {"name": "Betelgeuse", "constellation": "Orion", "distance": 642.5},
    {"name": "Proxima Centauri", "constellation": "Centaurus", "distance": 4.24}
]

with open("output_stars.yaml", "w") as file:
    yaml.dump(stars, file, default_flow_style=False)