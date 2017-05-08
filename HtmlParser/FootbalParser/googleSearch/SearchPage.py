from urllib.parse import unquote

from HtmlParser.common.SiteConnector import get_page

from HtmlParser.FootbalParser.googleSearch.urls import get_team_search_page_url

from lxml import etree

class SearchPage:
    def __init__(self, team_name):
        self.team_name = team_name

    def parse(self):
        current_page = get_page(get_team_search_page_url(self.team_name))
        # print(get_team_search_page_url(self.team_name))
        wiki_link_selector = '.b_algo a[href^="https://en.wikipedia"]'
        # wiki_link_selector = 'body'
        # print(etree.tostring(current_page.getroot(), pretty_print=True))
        # print(current_page.getroot().text_content())
        current_wiki_link = current_page.getroot().cssselect(wiki_link_selector)[0]
        current_name = current_wiki_link.text_content().replace('- Wikipedia', '')
        # if len(current_wiki_link.getchildren()) > 0:
        #     current_name = current_wiki_link.getchildren()[0].text
        #     print(current_name)
        # print(current_name)
        # current_name += current_wiki_link.text

        # print(current_wiki_link)
        current_name = unquote(current_name).replace('https://en.wikipedia.org/wiki/', '')
        # print(current_name)
        current_name = current_name.replace('_', ' ')
        return current_name



