from lxml import etree

# Create the root element
stars = etree.Element("stars")

# Add star elements with distance as a child node
sirius = etree.SubElement(stars, "star", name="Sirius", constellation="Canis Major")
etree.SubElement(sirius, "distance").text = "8.6"

proxima = etree.SubElement(stars, "star", name="Proxima Centauri", constellation="Centaurus")
etree.SubElement(proxima, "distance").text = "4.24"

# Convert to a string with pretty print
xml_string = etree.tostring(stars, pretty_print=True).decode()
print(xml_string)