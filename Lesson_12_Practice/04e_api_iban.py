# # https://api-ninjas.com/api
import requests
from ninja_secrets import API_KEY

iban = 'DE16200700000532013000'
api_url = 'https://api.api-ninjas.com/v1/iban?iban={}'.format(iban)
response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)