import time
from urllib.error import HTTPError

from HtmlParser.DotabuffParser.dotabuffParser.CsvWriter import *
from HtmlParser.DotabuffParser.dotabuffParser.DotabuffUrls import get_teams_url
from HtmlParser.DotabuffParser.dotabuffParser.TeamsMatchesPage import TeamsMatchesPage
from HtmlParser.common.SiteConnector import get_page

start_new_project()

teams_url = get_teams_url()
teams_page = get_page(teams_url)

table_selector = 'article.r-tabbed-table table'
match_info_table = teams_page.getroot().cssselect(table_selector)[0].getchildren()[1].getchildren()
teams_ids = []
for team in match_info_table:
    teams_ids.append(team.getchildren()[1].getchildren()[0].get('href').split('/')[-1])

parsed_data = {}
new_parsed_data = {}
should_wait = False
parsed_ids = []
for team_id in teams_ids:
    while team_id not in parsed_ids:
        try:
            new_page = TeamsMatchesPage(team_id, parsed_data)
            new_parsed_data = new_page.parse()
            parsed_data.update(new_parsed_data)
        except HTTPError as e:
            print(e, 'Let\'s wait')
            should_wait = True
        else:
            parsed_ids.append(team_id)
        finally:
            save_data(new_parsed_data)

        if should_wait:
            print('Current parsed ids: ', parsed_ids)
            time.sleep(60 * 60) # 1 hour wait for dotabuf allow requests
            should_wait = False

