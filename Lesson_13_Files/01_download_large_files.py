import requests


def download_file(target_url, local_filename=None):
    if local_filename is None:
        local_filename = target_url.split('/')[-1]
    with requests.get(target_url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                print('next_chunk')
                f.write(chunk)
    return local_filename


# download_file('https://brandslogos.com/wp-content/uploads/images/large/python-logo.png')
download_file('https://brandslogos.com/wp-content/uploads/images/large/python-logo.png', local_filename='python.png')
