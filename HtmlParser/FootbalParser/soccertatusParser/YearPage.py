from HtmlParser.common.SiteConnector import get_page
from HtmlParser.FootbalParser.soccertatusParser.urls import get_year_url
from HtmlParser.FootbalParser.soccertatusParser.ParsingConstants import PROPERTIES


class YearPage:
    def __init__(self, year_url):
        self.year_url = year_url

    def parse(self):
        print('Parsing year', self.year_url)
        year_page = get_page(get_year_url(self.year_url))

        table_selector = '.standings'
        standings_table = year_page.getroot().cssselect(table_selector)
        if (len(standings_table) == 0):
            return []
        standings_table = standings_table[0].getchildren()[1].getchildren()
        data = []
        for row in standings_table:
            current_tds = row.getchildren()
            i = 0
            current_data = {}
            current_data[PROPERTIES[i]] = current_tds[i].getchildren()[0].text
            i += 1
            for td in current_tds[1:]:
                current_data[PROPERTIES[i]] = td.text
                i += 1
            data.append(current_data)

        return data



