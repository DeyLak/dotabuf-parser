
LEAGUES = [
    'GB1', # Premier league
    'ES1', # La liga
    'L1', # Bundesliga
    'IT1', # Serie A
    'FR1', # Ligue 1
]

SEASON_WINTER = 'w'
SEASON_SUMMER = 's'

TRANSFER_WINDOWS = [
    SEASON_WINTER,
    SEASON_SUMMER,
]

NO_DATA = 'NO DATA'

FIRST_SEASON = 2016
LAST_SEASON = 1994

VALUABLE_TRANSFERS_COUNT = 3

TRANSFERS_TYPES = ['Arrival', 'Departure']

PROPERTIES = [
    'Total market value arrivals',
    'Expenditures',
    'Total market value departures',
    'Income',
]

NO_DATA_EXCLUDE_PROP = PROPERTIES[0] + ' - ' + SEASON_SUMMER

for type in TRANSFERS_TYPES:
    for i in range(VALUABLE_TRANSFERS_COUNT):
        PROPERTIES.append(type + str(i + 1))