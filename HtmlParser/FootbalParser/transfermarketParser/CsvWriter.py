import os

from HtmlParser.FootbalParser.transfermarketParser.ParsingConstants import PROPERTIES, TRANSFER_WINDOWS, NO_DATA_EXCLUDE_PROP, NO_DATA

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
        'Team',
    ]

    for transferWindow in TRANSFER_WINDOWS:
        for prop in PROPERTIES:
            csv_header.append('%s - %s' % (prop, transferWindow))

    exclude_prop_index = csv_header.index(NO_DATA_EXCLUDE_PROP) - 3

    str_result += ';'.join(csv_header) + '\n'

    for league in data.keys():
        current_league = data[league]
        for year in current_league.keys():
            current_year = current_league[year]
            part_year = int(year[:2])
            if part_year < 10:
                str_year = '200%s'
            elif part_year < 20:
                str_year = '20%s'
            else:
                str_year = '19%s'
            str_year = str_year % str(part_year)
            for team in current_year.keys():
                current_team = current_year[team]
                props = []
                for transferWindow in TRANSFER_WINDOWS:
                    if transferWindow not in current_team:
                        props += ['NO DATA' for _ in PROPERTIES]
                    else:
                        current_season = current_team[transferWindow]
                        new_props = [escape_csv_string(field) for field in current_season]
                        props += new_props
                if props[exclude_prop_index] == NO_DATA:
                    continue
                prefix = ';'.join([league, str_year, team])
                str_result += prefix + ';' + ';'.join(props) + '\n'

    with open(path_prefix + DEFAULT_RESULTS_FILE_NAME, "w", encoding='utf8') as f:
        f.write('\uFEFF' + str_result)
