from lxml import html

html_string = """
<html>
  <body>
    <div class="star" data-name="Sirius" data-constellation="Canis Major" data-distance="8.6"></div>
    <div class="star" data-name="Betelgeuse" data-constellation="Orion" data-distance="642.5"></div>
  </body>
</html>
"""

tree = html.fromstring(html_string)

# Extract star data using XPath
stars = tree.xpath('//div[@class="star"]')
for star in stars:
    name = star.get("data-name")
    constellation = star.get("data-constellation")
    distance = star.get("data-distance")
    print(f"{name} is in {constellation}, {distance} light-years away.")