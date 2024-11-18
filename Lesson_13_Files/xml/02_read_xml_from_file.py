from lxml import etree

# Parse the XML file
tree = etree.parse("stars.xml")
root = tree.getroot()

# Iterate through <star> nodes
for star in root.findall("star"):
    # Access attributes
    name = star.get("name")
    constellation = star.get("constellation")

    # Access child node text
    distance_node = star.find("distance")
    if distance_node is not None:
        distance = distance_node.text
    else:
        distance = "Unknown"

    print(f"{name} is in {constellation}, {distance} light-years away.")
