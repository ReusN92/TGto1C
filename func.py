from config import URL_PING, URL_APPROVE, LOGIN
from loguru import logger
import requests
import base64

headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6',
        'Authorization': f'Basic {base64.b64encode(bytes(f"{LOGIN}", "utf-8")).decode("ascii")}',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    }

def ping_pong():
    response = requests.get(URL_PING, headers=headers, verify=False)
    if response.status_code == 200:
        return response.json()
    else:
        data = {"result": f"Status Code [{response.status_code}]"}
        return data

def approve():
    response = requests.get(URL_APPROVE, headers=headers, verify=False)
    if response.status_code == 200:
        return response.json()
    else:
        data = {"result": f"Status Code [{response.status_code}]"}
        return data