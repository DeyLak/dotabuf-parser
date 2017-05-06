import os

from HtmlParser.FootbalParser.fifaParser.ParsingConstants import PROPERTIES


DEFAULT_RESULTS_FILE_NAME = 'etc/football/fifa.csv'

def start_new_project(path_prefix):
    if os.path.exists(DEFAULT_RESULTS_FILE_NAME):
        os.remove(DEFAULT_RESULTS_FILE_NAME)

def escape_csv_string(dangerous_string):
    string = dangerous_string.replace('\n', '')
    if ';' in string or '"' in string:
        return '"' + string.replace('"', '""') + '"'
    return string


def save_data(data, path_prefix):
    str_result = ''

    csv_header = [
        'Year',
    ]

    for prop in PROPERTIES:
        csv_header.append(prop)

    str_result += ';'.join(csv_header) + '\n'

    for year in data.keys():
        current_year = data[year]

        for entry in current_year:
            str_result += year + ';' + ';'.join([escape_csv_string(field) for field in entry]) + '\n'

    with open(path_prefix + DEFAULT_RESULTS_FILE_NAME, "w", encoding='utf8') as f:
        f.write('\uFEFF' + str_result)
