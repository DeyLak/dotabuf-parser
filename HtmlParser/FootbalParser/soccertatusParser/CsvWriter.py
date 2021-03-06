import os

from HtmlParser.FootbalParser.soccertatusParser.ParsingConstants import PROPERTIES


DEFAULT_RESULTS_FILE_NAME = 'etc/football/soccerstatus.csv'

def start_new_project(path_prefix):
    if os.path.exists(path_prefix + DEFAULT_RESULTS_FILE_NAME):
        os.remove(path_prefix + DEFAULT_RESULTS_FILE_NAME)

def escape_csv_string(string):
    if ';' in string or '"' in string:
        return '"' + string.replace('"', '""') + '"'
    return string

def save_data(data, path_prefix):
    str_result = ''

    csv_header = [
        'Country',
        'Year',
    ]

    for prop in PROPERTIES:
        csv_header.append(prop)

    str_result += ';'.join(csv_header) + '\n'

    for league in data.keys():
        current_league = data[league]
        for year in current_league.keys():
            current_year = current_league[year]
            str_year = year[:4]
            for entry in current_year:
                str_result += league + ';' + str_year + ';' + ';'.join([escape_csv_string(field) for field in entry.values()]) + '\n'

    with open(path_prefix + DEFAULT_RESULTS_FILE_NAME, "w", encoding='utf8') as f:
        f.write('\uFEFF' + str_result)
