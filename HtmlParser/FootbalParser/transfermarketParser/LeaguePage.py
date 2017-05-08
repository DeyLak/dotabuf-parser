import re

from HtmlParser.common.SiteConnector import get_page

from HtmlParser.FootbalParser.transfermarketParser.urls import get_league_url
from HtmlParser.FootbalParser.transfermarketParser.ParsingConstants import *
from HtmlParser.FootbalParser.googleSearch.index import get_team_name


MILLION = 'Mill.'
THOUSAND = 'Th.'

MONEY_ORDER_DICT = {
    MILLION : 1000000,
    THOUSAND: 1000,
}

def parse_money(text):
    if text == '-':
        return '0'
    number_to_parse = re.search(r'(\d+,?\d*) (' + MILLION + '|' + THOUSAND + ')', text)
    if number_to_parse is None:
        return '0'
    rounded = float(number_to_parse[1].replace(',', '.'))
    return str(rounded * MONEY_ORDER_DICT[number_to_parse[2]])

class LeaguePage:
    def __init__(self, league):
        self.league = league
        self.new_parsed_data = {}

    def parse(self):
        print('Parsing league', self.league)
        for year in range(FIRST_SEASON, LAST_SEASON, -1):
            print('Season', year)
            seasonText = str(year)[2:] + '/' + str(year + 1)[2:]
            nextSeasonText = str(year + 1)[2:] + '/' + str(year + 2)[2:]
            if seasonText not in self.new_parsed_data:
                self.new_parsed_data[seasonText] = {}
            if nextSeasonText not in self.new_parsed_data:
                self.new_parsed_data[nextSeasonText] = {}

            for transferWindow in TRANSFER_WINDOWS:
                print('Window', transferWindow)
                league_page = get_page(get_league_url(self.league, year, transferWindow))

                team_heuristic_selector = '.box'
                team_heuristic = league_page.getroot().cssselect(team_heuristic_selector)

                team_box_condition_selector = '.responsive-table'
                for box in team_heuristic:
                    team_condition = box.cssselect(team_box_condition_selector)
                    if (len(team_condition) == 0):
                        continue
                    team_name = get_team_name(box.getchildren()[0].getchildren()[1].text, self.league)
                    print('Team', team_name)


                    team_info = []

                    arrivals_info_selector = '.responsive-table + .transfer-zusatzinfo-box'
                    departures_info_selector = '.responsive-table > .transfer-zusatzinfo-box'

                    selectors = [arrivals_info_selector, departures_info_selector]
                    for i in range(len(TRANSFERS_TYPES)):
                        current_selector = selectors[i]
                        current_info = box.cssselect(current_selector)
                        if len(current_info) == 0:
                            team_info.append(NO_DATA)
                            team_info.append(NO_DATA)
                            continue

                        transfer_info = current_info[0].getchildren()
                        team_info.append(parse_money(transfer_info[1].text))
                        team_info.append(parse_money(transfer_info[2].text))

                    transfer_tables_selector = '.responsive-table > table > tbody'
                    transfer_tables = box.cssselect(transfer_tables_selector)
                    for i in range(len(TRANSFERS_TYPES)):
                        transfer_table = transfer_tables[i].getchildren()
                        for j in range(VALUABLE_TRANSFERS_COUNT):
                            if j >= len(transfer_table):
                                team_info.append(NO_DATA)
                                continue
                            current_player = transfer_table[j].getchildren()
                            if len(current_player) != 9:
                                team_info.append(NO_DATA)
                                continue
                            current_player = current_player[5]

                            team_info.append(parse_money(current_player.text))

                    if team_name not in self.new_parsed_data[seasonText]:
                        self.new_parsed_data[seasonText][team_name] = {}

                    if team_name not in self.new_parsed_data[nextSeasonText]:
                        self.new_parsed_data[nextSeasonText][team_name] = {}

                    if transferWindow == SEASON_WINTER:
                        current_season = nextSeasonText
                    else:
                        current_season = seasonText
                    self.new_parsed_data[current_season][team_name][transferWindow] = team_info

        return self.new_parsed_data



