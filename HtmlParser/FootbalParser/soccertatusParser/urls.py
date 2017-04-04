SOCCERSTATUS_ROOT = 'http://soccerstats.us'

def get_league_url(league):
    return '%s%s' %(SOCCERSTATUS_ROOT, league)

def get_year_url(year):
    return '%s%s' % (SOCCERSTATUS_ROOT, year)