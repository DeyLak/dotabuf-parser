DOTABUFF_ROOT = 'https://www.dotabuff.com'

def get_match_url(match_id):
    return '%s/matches/%s' %(DOTABUFF_ROOT, match_id)

def get_teams_url():
    return '%s/esports/teams' %(DOTABUFF_ROOT)

def get_teams_matches_url(team_id, page = 1):
    return '%s/esports/teams/%s/matches?page=%s' %(DOTABUFF_ROOT, team_id, page)
