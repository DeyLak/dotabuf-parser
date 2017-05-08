import lxml.html as html
import uuid
from urllib.request import urlopen, Request


def get_request_headers():
    return {
        'User-Agent' : str(uuid.uuid1()) + ' Not trying to DDOS, just parsing some data for statistics diploma :)',
    }

def get_page(url):
    if 'Users' in url:
        return html.parse(url)
    request = Request(url, headers=get_request_headers())
    return html.parse(urlopen(request))
