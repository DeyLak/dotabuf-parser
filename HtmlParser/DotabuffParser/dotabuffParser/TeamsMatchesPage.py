import re

from dateutil.parser import parse

from HtmlParser.DotabuffParser.dotabuffParser.DotaConstants import PATCH_700_DATE
from HtmlParser.DotabuffParser.dotabuffParser.DotabuffUrls import get_teams_matches_url
from HtmlParser.DotabuffParser.dotabuffParser.MatchPage import MatchPage
from HtmlParser.common.SiteConnector import get_page


class TeamsMatchesPage:
    def __init__(self, team_id, parsed_data):
        self.team_id = str(team_id)
        # self.team_id = str(2621843)
        self.parsed_data = parsed_data
        self.new_parsed_data = {}
        self.page_number = 0

    def parse(self):
        print('Parsing team', self.team_id)
        while self.page_number is not None:
            self.page_number += 1
            url = get_teams_matches_url(self.team_id, self.page_number)
            self.page = get_page(url)

            matches_table = self.page.getroot().cssselect('.recent-esports-matches')
            if (len(matches_table) == 0):
                break
            matches_table = matches_table[0].getchildren()[1].getchildren()
            for row in matches_table:
                current_td = row.getchildren()[1].getchildren()
                current_match_date = parse(current_td[1].getchildren()[0].get('datetime'))
                if PATCH_700_DATE > current_match_date:
                    self.page_number = None
                    break
                current_match_id = current_td[0].getchildren()[0].get('href').split('/')[-1]
                # Checking for match full players data, for some reason some matches have only one team
                opponent_team_td = row.getchildren()[5]
                if len(opponent_team_td.getchildren()[0].getchildren()) == 0:
                    print(current_match_id, 'doesn\'t have opponents team')
                    continue

                if (current_match_id not in self.parsed_data):
                    new_match = MatchPage(current_match_id)
                    self.new_parsed_data[current_match_id] = new_match.parse()
            table_counter = self.page.getroot().cssselect('div.viewport')[0].text
            counters = re.findall('\d+ - (\d+) of (\d+)', table_counter)
            if counters[0][0] == counters[0][1]:
                self.page_number = None
        return self.new_parsed_data




