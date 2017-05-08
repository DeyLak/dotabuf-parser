from urllib.parse import quote


site_path = 'https://yandex.ru/search/'
site_path = 'https://www.bing.com/search'

search_postfix = ' site:en.wikipedia.org football club wikipedia'

def get_team_search_page_url(search_string):
    formatted_search_string = quote(search_string + search_postfix)
    print('%s?q=%s' % (site_path, formatted_search_string))
    return '%s?q=%s' % (site_path, formatted_search_string)
