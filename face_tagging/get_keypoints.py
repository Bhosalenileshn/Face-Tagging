import requests
import json
import re

import numpy as np

URL = 'http://localhost:5000/getkeypts'


def get_keypts(image_url: str, silent: bool, method: str='docker'):
    if method == 'docker':
        f = {'file': open(image_url, 'rb').read()}
        result = requests.post(URL, files=f)
        if result.status_code == 200:
            try:
                keypts = json.loads(result.text)['points']
                keypts = np.array(keypts).reshape((1,-1))[0]
                return keypts
            except:
                return None
        else:
            if not silent: 
                print(result.text)
            return None
    else:
        raise ValueError("method not valid")