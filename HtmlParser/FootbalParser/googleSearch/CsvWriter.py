import os

from HtmlParser.FootbalParser.fotballStatisticsParser.ParsingConstants import PROPERTIES


FILE_NAME_PREFIX = 'teams_names-'

FILES_NAMES_PATH = 'etc/teams/'

DEFAULT_RESULTS_FILE_NAME = '%s%s%s.csv'

def get_file_name(country):
    return  DEFAULT_RESULTS_FILE_NAME % (FILES_NAMES_PATH, FILE_NAME_PREFIX, country)

def start_new_project(path_prefix, country):
    if os.path.exists(path_prefix + get_file_name(country)):
        os.remove(path_prefix + get_file_name(country))

def escape_csv_string(dangerous_string):
    if dangerous_string is None:
        return ''
    string = dangerous_string.replace('\n', '')
    if ';' in string or '"' in string:
        return '"' + string.replace('"', '""') + '"'
    return string


def save_data(data, path_prefix, country):
    str_result = ''

    csv_header = [
        'Replaced team',
    ]

    for team in data.keys():
        current_team = data[team]
        for i in range(len(csv_header), len(current_team) + 1):
            csv_header.append('Variant ' + str(i))

    for team in data.keys():
        current_team = data[team]
        values = list(current_team)
        for i in range(len(values), len(csv_header) - 1):
            values.append('')
        str_result += escape_csv_string(team) + ';' + ';'.join([escape_csv_string(field) for field in values]) + '\n'

    header_str = ';'.join(csv_header) + '\n'
    str_result = header_str + str_result
    with open(path_prefix + get_file_name(country), "w", encoding='utf8') as f:
        f.write('\uFEFF' + str_result)
