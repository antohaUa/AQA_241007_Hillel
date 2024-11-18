# pip install lxml
from lxml import etree

xml_string = """
<stars>
    <star name="Sirius" constellation="Canis Major" distance="8.6" />
    <star name="Betelgeuse" constellation="Orion" distance="642.5" />
</stars>
"""

root = etree.fromstring(xml_string)

# Access elements and attributes
for star in root.findall("star"):
    name = star.get("name")
    constellation = star.get("constellation")
    distance = star.get("distance")
    print(f"{name} is in {constellation}, {distance} light-years away.")