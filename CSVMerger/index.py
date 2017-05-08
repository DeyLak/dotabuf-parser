from CSVMerger.constants import *
from CSVMerger.CsvWriter import *
from HtmlParser.FootbalParser.googleSearch.index import get_team_name, output_teams_names


def merge_files(path_prefix):
    start_new_project(path_prefix)
    result = {}

    for file in BASE_FILES:
        current_dict = get_file_dict(file)
        for row in current_dict:
            current_year = row[YEAR_COLUMN]
            if current_year not in result:
                result[current_year] = {}

            country = row[LEAGUE_COLUMN]
            current_team = get_team_name(row[TEAM_COLUMN], country)
            if current_team not in result[current_year]:
                result[current_year][current_team] = {}
                result[current_year][current_team]['REPLACED_TEAM ' + file] = row[TEAM_COLUMN]
            for key in row.keys():
                if key == YEAR_COLUMN or key == TEAM_COLUMN:
                    continue
                result[current_year][current_team][key] = row[key]

    for file in FILES:
        current_dict = get_file_dict(file)

        for row in current_dict:
            current_year = row[YEAR_COLUMN]
            if current_year not in result:
                continue

            country = row[LEAGUE_COLUMN]
            current_team = get_team_name(row[TEAM_COLUMN], country)
            if current_team not in result[current_year]:
                continue
            result[current_year][current_team]['REPLACED_TEAM ' + file] = row[TEAM_COLUMN]
            for key in row.keys():
                if key == YEAR_COLUMN or key == TEAM_COLUMN:
                    continue
                result[current_year][current_team][key] = row[key]

    save_data(result, path_prefix)
    output_teams_names(path_prefix)

if __name__ == '__main__':
    merge_files('../')