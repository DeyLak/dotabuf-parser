import os

from HtmlParser.FootbalParser.fotballStatisticsParser.ParsingConstants import PROPERTIES


DEFAULT_RESULTS_FILE_NAME = 'etc/forMerge/result.csv'

def start_new_project(path_prefix):
    if os.path.exists(path_prefix + DEFAULT_RESULTS_FILE_NAME):
        os.remove(path_prefix + DEFAULT_RESULTS_FILE_NAME)

def escape_csv_string(dangerous_string):
    if dangerous_string is None:
        return ''
    try:
        float(dangerous_string)
    except ValueError:
        pass
    string = dangerous_string.replace('\n', '')
    if ';' in string or '"' in string:
        return '"' + string.replace('"', '""') + '"'
    return string


def save_data(data, path_prefix):
    str_result = ''

    csv_header = [
        'Year',
        'Team',
    ]

    keys = []
    for year in data:
        for team in data[year]:
            keys = set(list(keys) + list(data[year][team].keys()))
    csv_header += keys

    str_result += ';'.join(csv_header) + '\n'

    for year in data.keys():
        current_year = data[year]
        for team in current_year.keys():
            current_team = current_year[team]
            current_row = []
            for key in keys:
                if key in current_team:
                    current_row.append(current_team[key])
                else:
                    current_row.append('EMPTY_MERGE_CELL')

            str_result += year + ';' + escape_csv_string(team) + ';' + ';'.join([escape_csv_string(field) for field in current_row]) + '\n'

    with open(path_prefix + DEFAULT_RESULTS_FILE_NAME, "w", encoding='utf8') as f:
        f.write('\uFEFF' + str_result)
