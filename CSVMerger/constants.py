import csv


root_path = '/Users/deylak/Desktop/ForLovelyMe/Repository/sites-parser/etc/forMerge/'

BASE_FILES = [
    'soccerstatus-not-shifted.csv',
    'hand-made-not-shifted.csv',
]

FILES = [
    'fifa.csv',
    'fotballStatistics-not-shifted.csv',
    'fotballStatistics-shifted.csv',
    'soccerstatus-shifted.csv',
    'transfermarket.csv',
    'hand-made-shifted.csv',
]

def get_file_dict(name):
    with open('%s%s' % (root_path, name), 'r') as f:
        dialect = csv.Sniffer().sniff(f.read(), delimiters=';')
        f.seek(0)
        return [row for row in csv.DictReader(f, dialect=dialect)]

YEAR_COLUMN = 'Year'
TEAM_COLUMN = 'Team'
LEAGUE_COLUMN = 'Country'