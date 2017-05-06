from urllib.parse import quote


site_path = 'https://yandex.ru/search/'

search_postfix = ' футбольный клуб википедия'

def get_team_search_page_url(search_string):
    formatted_search_string = quote(search_string + search_postfix)

    return '%s?text=%s' % (site_path, formatted_search_string)