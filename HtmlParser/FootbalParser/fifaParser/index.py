import time
from urllib.error import HTTPError

from HtmlParser.common.ConvertingFunctions import to_text_season

from HtmlParser.FootbalParser.fifaParser.CsvWriter import *
from HtmlParser.FootbalParser.fifaParser.ParsingConstants import *
from HtmlParser.FootbalParser.fifaParser.YearPage import YearPage


def parse_fifa(path_prefix = './'):
    start_new_project(path_prefix)

    parsed_data = {}
    should_wait = False
    parsed_years = []

    for year in YEARS:
        while year not in parsed_years:
            try:
                current_season = STARTING_SEASON - YEARS.index(year)
                text_season = to_text_season(current_season)
                print('Parsing season', text_season)
                new_league = YearPage(text_season.split('/')[1], year)
                new_parsed_data = new_league.parse()
                parsed_data[text_season] = new_parsed_data
            except HTTPError as e:
                print(e, 'Let\'s wait')
                should_wait = True
            else:
                parsed_years.append(year)
            finally:
                save_data(parsed_data, path_prefix)

            if should_wait:
                print('Current parsed leagues: ', parsed_years)
                time.sleep(60 * 60) # 1 hour wait for site allow requests
                should_wait = False


if __name__ == '__main__':
    parse_fifa('../../../')