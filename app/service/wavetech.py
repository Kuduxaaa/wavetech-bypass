import requests
import subprocess
import json
import base64
import os
import sys
import time

from fake_useragent import UserAgent

API_URL = 'https://api.wavetech.ai/v1/landing'

def _get_session(new_ip=False):
    if new_ip:
        time.sleep(.3)
        subprocess.call(['sudo', 'service', 'tor', 'restart'], stdout=subprocess.PIPE)

    session = requests.session()
    session.proxies = dict(http = 'socks5://127.0.0.1:9050',
                            https = 'socks5://127.0.0.1:9050')

    session.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
        'Origin': 'https://wavetech.ai',
        'Referer': 'https://wavetech.ai/',
        'Connection': 'keep-alive'
    }

    return session


def check_host():
    session = _get_session()
    try:
        response = session.get('https://wavetch.ai')
        if response.ok:
            return True
    except Exception as e:
        return False
    
    return False

def get_audio(text, version='ge_m0', new_ip=False):
    session = _get_session()
    
    if new_ip:
        session = _get_session(new_ip=True)
    
    try:
        data = None
        while data is None:
            response = session.post(API_URL, json={'text': text, 'version': version}, timeout=5)
            _data = json.loads(response.text)

            if 'file' not in _data:
                session = _get_session(new_ip=True)
            else:
                data = _data
        
        return data
        
    except requests.exceptions.ConnectionError:
        return get_audio(text, version, True)
        
    except Exception as e:
        return {
            'message': e,
            'code': 500
        }
        
# if not check_host():
    # print('[!] Host is not reachable')
    # sys.exit(1)