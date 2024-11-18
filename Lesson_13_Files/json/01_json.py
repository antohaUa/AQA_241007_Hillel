# JSON (JavaScript Object Notation) is a lightweight data-interchange format
# https://www.json.org/json-en.html
# https://en.wikipedia.org/wiki/JSON
# https://docs.python.org/3/library/json.html

import json
import pprint
#
# # load from file
try:
    with open('data_light.json', 'r') as json_fh:
        result = json.load(json_fh)  # python dictionary
        print(result)
        print(type(result))
except json.decoder.JSONDecodeError as j_err:
    print(j_err)
    print('Wrong format')
#
# # load from structure
# s1 = """
# {
#   "firstName": "John",
#   "lastName": "Smith",
#   "isAlive": true,
#   "age": 27,
#   "address": {
#     "streetAddress": "21 2nd Street",
#     "city": "New York",
#     "state": "NY",
#     "postalCode": "10021-3100"
#     }
#   }
# """
# result = json.loads(s1)
# print(type(result))
# # print(result)
# pprint.pprint(result)

# dumps
d1 = {'results': [{'gender': 'male', 'name': {'title': 'Mr', 'first': 'Jerry', 'last': 'Lambert'}}]}
print(json.dumps(d1, indent=4))

# dump
with open('out.json', 'wt') as json_fh:
    json.dump(d1, json_fh, indent=4)


# # json errors
#
