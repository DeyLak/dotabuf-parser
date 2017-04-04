import os

from HtmlParser.FootbalParser.transfermarketParser.ParsingConstants import PROPERTIES


DEFAULT_RESULTS_FILE_NAME = 'etc/football/transfermarket.csv'

def start_new_project(path_prefix):
    if os.path.exists(DEFAULT_RESULTS_FILE_NAME):
        os.remove(DEFAULT_RESULTS_FILE_NAME)

def escape_csv_string(string):
    if ';' in string or '"' in string:
        return '"' + string.replace('"', '""') + '"'
    return string


def save_data(data, path_prefix):
    str_result = ''

    csv_header = [
        'League',
        'Year',
        'Season',
        'Team',
    ]

    for prop in PROPERTIES:
        csv_header.append(prop)

    str_result += ';'.join(csv_header) + '\n'

    for league in data.keys():
        current_league = data[league]
        for year in current_league.keys():
            current_year = current_league[year]
            for season in current_year.keys():
                current_season = current_year[season]
                for team in current_season.keys():
                    current_team = current_season[team]
                    prefix = ';'.join([league, year, season, team])
                    str_result += prefix + ';' + ';'.join([escape_csv_string(field) for field in current_team]) + '\n'

    with open(path_prefix + DEFAULT_RESULTS_FILE_NAME, "w", encoding='utf8') as f:
        f.write('\uFEFF' + str_result)
