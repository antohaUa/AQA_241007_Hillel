import requests
from requests.exceptions import HTTPError
from ninja_secrets import API_KEY

api_url = 'https://api.api-ninjas.com/v1/imagetotext'

try:
    with open('scan.png', 'rb') as r_fh:
        files = {'image': r_fh}
        headers = {'X-Api-Key': API_KEY}
        response = requests.post(api_url, files=files, timeout=10, headers=headers)
        response.raise_for_status()
        data = response.json()
        collected_data = [itm.get('text') for itm in data]
        str_text = ' '.join(collected_data)
        print(str_text)
except HTTPError as http_err:
    pass
