# # https://api-ninjas.com/api
import requests
from bucket.ninja_secrets import API_KEY

QR_URL = 'https://api.api-ninjas.com/v1/qrcode'


def qrcode(data):
    try:
        params = {'format': 'png', 'data': data, 'fg_color': '00ff00'}
        response = requests.get(QR_URL, params=params, timeout=10,
                                headers={'X-Api-Key': API_KEY, 'Accept': 'image/png'})
        response.raise_for_status()
        return response.content
    except Exception as g_exc:
        pass
    # if response.status_code == 200:
    #     return response.content
    # return 'Error'


def save_to_file(filename, content):
    with open(filename, 'wb') as fh:
        # shutil.copyfileobj(content, fh)
        fh.write(content)
    print('File saved')


cont = qrcode('https://api-ninjas.com')
# print(cont)
save_to_file('001.png', cont)
