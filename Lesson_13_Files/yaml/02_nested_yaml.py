import yaml


with open("nested_stars.yaml", "r") as file:
    data = yaml.safe_load(file)
    for star, details in data.items():
        print(f"{star} is in {details['constellation']} and is {details['distance']} light-years away.")


stars = {
    "Sirius": {"constellation": "Canis Major", "distance": 8.6},
    "Betelgeuse": {"constellation": "Orion", "distance": 642.5},
}

yaml_string = yaml.dump(stars, default_flow_style=False, sort_keys=False)
print(yaml_string)