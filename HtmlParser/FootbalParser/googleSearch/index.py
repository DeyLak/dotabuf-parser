import glob, csv

from HtmlParser.FootbalParser.googleSearch.SearchPage import SearchPage
from HtmlParser.FootbalParser.googleSearch.CsvWriter import *
from pymongo import MongoClient

parsed_names = MongoClient().football.teams

def get_team_name(bad_name, country = 'NO_COUNTRY'):
    print('getting team name', bad_name)
    name = parsed_names.find_one({ '_id': bad_name })
    if name is not None:
        current_team_name = name['replace_name']
    else:
        name = parsed_names.find_one({ '_id': bad_name.strip() })
        if name is not None:
            current_team_name = name['replace_name']
        else:
            name = parsed_names.find_one({ 'replace_name': bad_name })
            if name is not None:
                current_team_name = name['replace_name']
            else:
                name = parsed_names.find_one({ 'replace_name': bad_name.strip() })
                if name is not None:
                    current_team_name = name['replace_name']
                else:
                    current_team_name = SearchPage(bad_name).parse()
                    parsed_names.insert_one({
                        '_id': bad_name,
                        'replace_name': current_team_name,
                        'country': country,
                    })
    return current_team_name

def run_teams_search(path_prefix = '.'):
    with open(path_prefix + 'input.txt', "r") as f:
        teams = [team.replace('\n', '') for team in f.readlines()]
    result = []
    for team in teams:
        result.append(get_team_name(team))
    with open(path_prefix + 'output.txt', "w") as f:
        for team in result:
            f.write('%s\n' % team)

def output_teams_names(path_prefix = ''):
    replaced_dict = {}
    for team in parsed_names.find():
        current_name = team['replace_name']
        current_country = team['country']
        if current_country not in replaced_dict:
            replaced_dict[current_country] = {}
        if current_name not in replaced_dict[current_country]:
            replaced_dict[current_country][current_name] = []
        replaced_dict[current_country][current_name].append(team['_id'])

    for country in replaced_dict.keys():
        start_new_project(path_prefix, country)
        save_data(replaced_dict[country], path_prefix, country)


def parse_teams_names(path_prefix):
    print(FILES_NAMES_PATH + '*.csv')
    for file in glob.glob(path_prefix + FILES_NAMES_PATH + '*.csv'):
        current_country = file.split('/')[-1].split('.')[0].replace(FILE_NAME_PREFIX, '')
        print('Parsing', current_country)
        with open(file, "r", encoding='utf8') as f:
            dialect = csv.Sniffer().sniff(f.read(), delimiters=';')
            f.seek(0)
            for row in csv.DictReader(f, dialect=dialect):
                values = list(row.values())
                replace_name = values[0]
                for team in values[1:]:
                    if parsed_names.find_one({ '_id': team }) is not None:
                        parsed_names.update({ '_id': team }, {
                            'replace_name': replace_name,
                            'country': current_country,
                        })
                    else:
                        parsed_names.insert_one({
                            '_id': team,
                            'replace_name': replace_name,
                            'country': current_country,
                        })

if __name__ == '__main__':
    parse_teams_names('../../../')
    # run_teams_search('../../../')
    # output_teams_names('../../../')