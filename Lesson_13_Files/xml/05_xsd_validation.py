from lxml import etree

# Load and parse the XSD schema
with open("stars.xsd", "r") as schema_file:
    schema_root = etree.XML(schema_file.read())
    schema = etree.XMLSchema(schema_root)

# Parse the XML document
with open("stars.xml", "r") as xml_file:
    xml_tree = etree.parse(xml_file)

# Validate the XML document against the schema
try:
    schema.assertValid(xml_tree)
    print("XML is valid according to the schema.")
except etree.DocumentInvalid as e:
    print(f"XML is invalid: {e}")