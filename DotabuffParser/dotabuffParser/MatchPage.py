from dotabuffParser.DotabuffConnector import get_page
from dotabuffParser.DotabuffUrls import get_match_url
from dotabuffParser.HtmlParsingHelpers import get_table_row_names, parse_table_row
from dotabuffParser.DotubuffParsingConstants import *
from dotabuffParser.DotaConstants import TEAMS


BAD_MATCHES = []

class MatchPage:
    def __init__(self, match_id):
        self.match_id = str(match_id)
        # self.match_id = '2929995330'

    def parse_team_results(self):
        result = {}
        for team in TEAMS:
            team_selector = 'section.' + team
            table_selector = team_selector  + ' > article.r-tabbed-table > table'
            match_info_table = self.page.getroot().cssselect(table_selector)[0].getchildren()
            #getting necessary tr tag according to table structure
            col_names = get_table_row_names(match_info_table[0].getchildren()[0])
            team_result = []
            for row in match_info_table[1].getchildren():
                team_result.append(parse_table_row(row, col_names))

            header_selector = team_selector + ' > header'
            header_elem = self.page.getroot().cssselect(header_selector)[0]

            team_name = header_elem.text if header_elem.text is not None else header_elem.cssselect('.esports-link')[0].text
            result[team] = {
                'values': team_result,
                'name': team_name,
            }
        self.team_results = result
        return result

    def parse_winner(self):
        for team in TEAMS:
            selector = '.match-result.team.' + team
            if self.page.getroot().cssselect(selector):
                self.winner = team
                return self.winner

    def parse_match_info(self):
        info = self.page.getroot().cssselect('.header-content-secondary')[0].getchildren()
        for item in info:
            children = item.getchildren()
            currentText = children[1].text
            if (currentText == 'Duration'):
                self.duration = children[0].text
            if (currentText == 'Match Ended'):
                self.end_time = children[0].getchildren()[0].get('datetime')

    def get_team_name(self, team):
        return self.team_results[team]['name']

    def get_team_field(self, team, field):
        result = []
        for value in self.team_results[team]['values']:
            if field in value:
                result.append(value[field])
            else:
                result.append('NO DATA')
        return result

    def get_result_data(self):
        result = []

        result.append(str(self.match_id))
        result.append(str(self.end_time))
        result.append(str(self.duration))
        result.append(str(self.winner))
        for team in TEAMS:
            result.append(str(self.get_team_name(team)))

        for field in RESULT_VALUES_ORDER:
            for team in TEAMS:
                values = self.get_team_field(team, field)
                for value in values:
                    result.append(str(value))
        return result


    def parse(self):
        print('Parsing match', self.match_id)
        if (self.match_id in BAD_MATCHES):
            print('Bad match!')
            return []
        url = get_match_url(self.match_id)
        self.page = get_page(url)

        self.parse_team_results()
        self.parse_winner()
        self.parse_match_info()

        return self.get_result_data()





