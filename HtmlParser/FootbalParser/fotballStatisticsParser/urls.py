import os


site_path = '/Users/deylak/Desktop/ForLovelyMe/httprack/footbal/www.european-football-statistics.co.uk/attn/'

class LeagueFileNotFoundException(Exception):
    pass

def get_current_year_file(league):
    file_path = '%save%s.html' % (site_path, league)
    if os.path.exists(file_path):
        return file_path
        # with open(file_path, "r") as f:
        #     return f.read()
    raise LeagueFileNotFoundException('No league %s for current year file found!' % league)

def get_archive_file(league, year):
    year_for_path = str(year)
    years_to_try = [
        year_for_path,
        year_for_path[2:],
    ]
    for str_year in years_to_try:
        file_path = '%sarchive/%s/ave%s%s.html' % (site_path, league, league, str_year)
        if os.path.exists(file_path):
            return file_path
            # with open(file_path, "r") as f:
            #     return f.read()
    raise LeagueFileNotFoundException('No league %s for %s year file found!' % (league, year))