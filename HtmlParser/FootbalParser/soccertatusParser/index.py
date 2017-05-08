import traceback
import time
from urllib.error import HTTPError

from HtmlParser.FootbalParser.soccertatusParser.CsvWriter import *
from HtmlParser.FootbalParser.soccertatusParser.ParsingConstants import LEAGUES, LEAGUES_DICT
from HtmlParser.FootbalParser.soccertatusParser.LeaguePage import LeaguePage


def parse_soccerstatus(path_prefix = './'):
    start_new_project(path_prefix)

    parsed_data = {}
    should_wait = False
    parsed_leagues = []

    for league in LEAGUES:

        while league not in parsed_leagues:
            try:
                new_league = LeaguePage(league)
                new_parsed_data = new_league.parse()
                parsed_data[LEAGUES_DICT[league]] = new_parsed_data
            except HTTPError as e:
                print(e, 'Let\'s wait')
                should_wait = True
            else:
                parsed_leagues.append(league)
            finally:
                save_data(parsed_data, path_prefix)

            if should_wait:
                print('Current parsed leagues: ', parsed_leagues)
                time.sleep(60 * 60) # 1 hour wait for site allow requests
                should_wait = False

if __name__ == '__main__':
    parse_soccerstatus('../../../')