import os
import requests

from HtmlParser.common.SiteConnector import get_request_headers

TRANSFERMARKET_ROOT = 'http://www.transfermarkt.com/jumplist/transfers/wettbewerb/'

cache_path = '/Users/deylak/Desktop/ForLovelyMe/Repository/sites-parser/etc/cache/'

def get_file_name(league, year, season):
    return '{}-{}-{}.html'.format(league, year, season)

def get_league_url(league, year, season):
    file_name = cache_path + get_file_name(league, year, season)
    url = '%s%s?saison_id=%s&s_w=%s' %(TRANSFERMARKET_ROOT, league, year, season)
    print(url)
    if os.path.exists(file_name):
        return file_name
    else:
        file = requests.get(url, headers=get_request_headers())
        with open(file_name, "w", encoding='utf8') as f:
            print(file_name)
            f.write(file.content.decode('utf-8'))
    return url
