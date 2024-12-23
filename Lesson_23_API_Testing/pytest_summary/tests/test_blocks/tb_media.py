import logging
import os.path

_log = logging.getLogger('Main')

import requests
from pytest_plugin import Cfg

PNG_1 = Cfg.params.get('png_1')
LOCAL_PNG_1 = 'test_man.png'
PNG_HEADER = b'\x89PNG'


class TestMedia:
    __test__ = False

    @staticmethod
    def download_file(target_url, local_filename=None):
        if local_filename is None:
            local_filename = target_url.split('/')[-1]
        with requests.get(target_url, stream=True) as response:
            if not response.status_code == 200:
                _log.warning(response.status_code)
                _log.warning(response.text)
                return ''
            with open(local_filename, 'wb') as fh:
                for chunk in response.iter_content(chunk_size=8192):
                    fh.write(chunk)
        return local_filename

    def test_download_file(self):
        assert self.download_file(PNG_1, local_filename=LOCAL_PNG_1) != '', 'Media download failed'

    def test_media_is_png(self):
        assert os.path.exists(LOCAL_PNG_1), 'Target PNG file not found'
        assert os.path.isfile(LOCAL_PNG_1), 'Not file'
        with open(LOCAL_PNG_1, 'rb') as png_fh:
            header = png_fh.read(4)
            assert header == PNG_HEADER, f'Incorrect header {header}'
