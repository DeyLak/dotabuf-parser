import time
import lxml.html as html
from urllib.error import HTTPError

from HtmlParser.FootbalParser.fotballStatisticsParser.CsvWriter import *
from HtmlParser.FootbalParser.fotballStatisticsParser.ParsingConstants import *
from HtmlParser.FootbalParser.fotballStatisticsParser.urls import *
from HtmlParser.FootbalParser.fotballStatisticsParser.YearPage import YearPage


def parse_fotball_statistics(path_prefix = './'):
    start_new_project(path_prefix)

    parsed_data = {}
    should_wait = False
    parsed_leagues = []

    for league in LEAGUES:
        while league not in parsed_leagues:
            try:
                print('Parsing league', league)
                parsed_data[league] = {}
                for year in range(START_YEAR, END_YEAR + 1):
                    print('Parsing year', year)
                    try:
                        if year == CURRENT_YEAR:
                            current_file = get_current_year_file(league)
                        else:
                            current_file = get_archive_file(league, year)
                        year_page = YearPage(html.parse(current_file))

                        parsed_data[league][str(year)] = year_page.parse()
                    except LeagueFileNotFoundException as e:
                        print('Not found!')
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
    parse_fotball_statistics('../../../')