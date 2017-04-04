import os

from HtmlParser.DotabuffParser.dotabuffParser.DotubuffParsingConstants import RESULT_VALUES_ORDER
from HtmlParser.DotabuffParser.dotabuffParser.DotaConstants import TEAMS, PLAYERS_COUNT


DEFAULT_RESULTS_FILE_NAME = '../../etc/matches.csv'

def start_new_project():
    if os.path.exists(DEFAULT_RESULTS_FILE_NAME):
        os.remove(DEFAULT_RESULTS_FILE_NAME)

def escape_csv_string(string):
    if ';' in string or '"' in string:
        return '"' + string.replace('"', '""') + '"'
    return string

def save_data(data):
    str_result = ''
    if not os.path.exists(DEFAULT_RESULTS_FILE_NAME):
        with open(DEFAULT_RESULTS_FILE_NAME, "w", encoding='utf8') as f:
            f.write('\uFEFF')

        csv_header = [
            'Match id',
            'End time',
            'Duration',
            'Winner'
        ]

        for team in TEAMS:
            csv_header.append('Team '+ team)

        for value in RESULT_VALUES_ORDER:
            for team in TEAMS:
                for player_number in range(PLAYERS_COUNT):
                    csv_header.append('Team ' + team + ' ' + value + ' #' + str(player_number + 1))

        str_result += ';'.join(csv_header) + '\n'

    for match in data.values():
        str_result += ';'.join([escape_csv_string(field) for field in match]) + '\n'

    with open(DEFAULT_RESULTS_FILE_NAME, "a", encoding='utf8') as f:
        f.write(str_result)
