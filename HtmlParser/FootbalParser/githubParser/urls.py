import os


site_path = '/Users/deylak/Desktop/ForLovelyMe/eng-england-master/'

class LeagueFileNotFoundException(Exception):
    pass

def get_league_file(year, league):
    str_year = str(year)
    s_year = '%s0s' % str_year[:3]
    decade = int(str_year[2:])
    year_folder_name = '%s-%s' % (str_year, decade)
    file_path = '%save%s.html' % (site_path, league)
    if os.path.exists(file_path):
        return file_path
        # with open(file_path, "r") as f:
        #     return f.read()
    raise LeagueFileNotFoundException('No league %s for current year file found!' % league)
