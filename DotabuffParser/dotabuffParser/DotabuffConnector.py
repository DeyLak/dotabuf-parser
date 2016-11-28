import lxml.html as html
from urllib.request import urlopen, Request


REQUEST_HEADERS = {
    'User-Agent' : 'Not trying to DDOS, just parsing some data for statistics diploma :)',
}

def get_page(url):
    request = Request(url, headers=REQUEST_HEADERS)
    return html.parse(urlopen(request))
