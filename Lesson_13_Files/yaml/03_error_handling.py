import yaml

try:
    with open("invalid_stars.yaml", "r") as file:
        data = yaml.safe_load(file)
        print(data)
except yaml.YAMLError as yaml_err:
    print(f"Error parsing YAML: {yaml_err}")