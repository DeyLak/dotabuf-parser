TRANSFERMARKET_ROOT = 'http://www.transfermarkt.com/jumplist/transfers/wettbewerb/'

def get_league_url(league, year, season):
    return '%s%s?saison_id=%s&s_w=%s' %(TRANSFERMARKET_ROOT, league, year, season)
