import requests

from config import settings


def make_request():
    flask_settings = settings.get("flask")

    url = f"http://{flask_settings.get('host')}:{flask_settings.get('port')}/recognize"
    print(requests.post(url=url, data="Hello, World"))
