import re

from HtmlParser.common.SiteConnector import get_page

from HtmlParser.FootbalParser.fifaParser.ParsingConstants import *
from HtmlParser.FootbalParser.fifaParser.urls import get_teams_url

MILLION = 'M'
THOUSAND = 'K'

MONEY_ORDER_DICT = {
    MILLION : 1000000,
    THOUSAND: 1000,
}

def parse_money(text):
    if text == '-':
        return '0'
    number_to_parse = re.search(r'(\d+\.?\d*)(' + MILLION + '|' + THOUSAND + ')', text)
    if number_to_parse is None:
        return '0'
    rounded = float(number_to_parse[1])
    return str(rounded * MONEY_ORDER_DICT[number_to_parse[2]])

class YearPage:
    def __init__(self,season, year_stamp):
        self.year_stamp = year_stamp
        self.season = season
        self.offset = 0
        self.new_parsed_data = []

    def parse(self):
        while self.offset is not None:
            print('Parsing offset', self.offset)

            current_page = get_page(get_teams_url(self.season, self.year_stamp, self.offset))

            teams_table_selector = '.card > table > tbody'
            teams_table = current_page.getroot().cssselect(teams_table_selector)[0].getchildren()

            for row in teams_table:
                new_data = []
                team_name = row[0].getchildren()[1].text
                new_data.append(team_name)

                team_country = row[1].getchildren()[0].getchildren()[0].get('title')
                new_data.append(team_country)

                for i in range(2, 6):
                    new_data.append(row[i].getchildren()[0].text)

                new_data.append(row[6].text)
                for i in range(7, 9):
                    new_data.append(row[i].getchildren()[0].text)

                new_data.append(parse_money(row[9].text))
                self.new_parsed_data.append(new_data)

            next_button_selector = '.card-footer > .pagination'
            next_button_url = current_page.getroot().cssselect(next_button_selector)[0].getchildren()[1].getchildren()[0].get('href')
            offset = re.search(r'offset=(\d+)', next_button_url)
            if offset is None:
                break
            self.offset = offset[1]

        return self.new_parsed_data



