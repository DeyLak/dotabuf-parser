DOTABUFF_ROOT = 'https://www.dotabuff.com'

def get_match_url(match_id):
    return '%s/matches/%s' %(DOTABUFF_ROOT, match_id)
