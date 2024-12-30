# http://xpather.com/
# https://www.selenium.dev/documentation/webdriver/elements/finders/

# https://www.w3schools.com/xml/xpath_axes.asp


# Select element by absolute XPath:
# /html/body/div/div[2]/form/input[1]

# Select element by relative XPath (starts from current node):
# ./div[@class='container']/ul/li

# Select element by tag name:
# //div

# Select element by ID:
# //*[@id='element_id']

# Select element by class name:
# //*[contains(@class, 'class_name')]

# Select element by attribute value:
# //*[@attribute_name='value']

# Select element by attribute value containing a certain string:
# //*[@attribute_name[contains(., 'partial_value')]]

# Select the first occurrence of an element:
# (//*[@attribute_name='value'])[1]

# Select the last occurrence of an element:
# (//*[@attribute_name='value'])[last()]

# Select parent element:
# //*[text()='text']/..

# Select following sibling:
# //*[text()='text']/following-sibling::*

# Select preceding sibling:
# //*[text()='text']/preceding-sibling::*

# Select element by text content:
# //*[text()='text']
