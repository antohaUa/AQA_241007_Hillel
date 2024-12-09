import requests


# download large files
def download_large_file(target_url, local_filename=None):
    if local_filename is None:
        local_filename = target_url.split('/')[-1]
    with requests.get(target_url, stream=True) as resp:
        resp.raise_for_status()
        with open(local_filename, 'wb') as f:
            for idx, chunk in enumerate(resp.iter_content(chunk_size=8192)):
                print(f'Chunk={idx}')
                f.write(chunk)
    return local_filename


download_large_file('https://freebiehive.com/wp-content/uploads/2023/08/Butterfly-PNG-1-758x473.jpg',
                    local_filename='butterfly.png')
