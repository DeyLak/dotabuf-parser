from HtmlParser.common.SiteConnector import get_page

from HtmlParser.FootbalParser.soccertatusParser.urls import get_league_url
from HtmlParser.FootbalParser.soccertatusParser.YearPage import YearPage


class LeaguePage:
    def __init__(self, league):
        self.league = league
        # self.team_id = str(2621843)
        self.new_parsed_data = {}

    def parse(self):
        print('Parsing league', self.league)
        league_page = get_page(get_league_url(self.league))

        table_selector = '#content table'
        league_years_table = league_page.getroot().cssselect(table_selector)[0].getchildren()
        for row in league_years_table[1:]:
            current_year = row.getchildren()[0].getchildren()[0]

            year_page = YearPage(current_year.get('href'))
            self.new_parsed_data[current_year.text] = year_page.parse()

        return self.new_parsed_data



