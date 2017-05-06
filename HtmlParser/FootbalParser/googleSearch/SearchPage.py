from urllib.parse import unquote

from HtmlParser.common.SiteConnector import get_page

from HtmlParser.FootbalParser.googleSearch.urls import get_team_search_page_url


class SearchPage:
    def __init__(self, team_name):
        self.team_name = team_name

    def parse(self):
        current_page = get_page(get_team_search_page_url(self.team_name))
        wiki_link_selector = '.serp-item a[href^="https://ru.wikipedia"]'
        current_wiki_link = current_page.getroot().cssselect(wiki_link_selector)[0].get('href')
        current_name = unquote(current_wiki_link).replace('https://ru.wikipedia.org/wiki/', '')
        current_name = current_name.replace('_', ' ')
        return current_name



