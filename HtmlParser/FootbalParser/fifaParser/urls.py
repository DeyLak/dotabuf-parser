from HtmlParser.FootbalParser.fifaParser.ParsingConstants import *

FIFA_ROOT = 'http://sofifa.com/teams'

leagues_params = '&'.join(['lg%5B' + str(i)+ '%5D=' + str(league) for i, league in enumerate(LEAGUES)])


def get_teams_url(season, year_stamp, offset = 0):
    return '%s?e=%s&%s&offset=%s&v=%s' %(FIFA_ROOT, year_stamp, leagues_params, offset, season)
