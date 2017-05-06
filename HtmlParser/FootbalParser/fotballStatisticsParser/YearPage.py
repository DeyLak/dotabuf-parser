import re

from HtmlParser.FootbalParser.fotballStatisticsParser.ParsingConstants import *


class YearPage:
    def __init__(self, html):
        self.html = html

    def parse(self):
        new_parsed_data = []

        first_table_selector = 'table'
        first_league_table = self.html.getroot().cssselect(first_table_selector)[2].getchildren()[1:]

        current_headers = [re.sub('\s', '', td.text) for td in first_league_table[0].getchildren()]

        first_division_index = None
        if DIVISION_HEADER_NAME in current_headers:
            first_division_index = current_headers.index(DIVISION_HEADER_NAME)

        properties_indecies = []
        for header_name in current_headers:
            if header_name in PROPERTIES:
                properties_indecies.append(current_headers.index(header_name))
        first_division_name = None

        prop_regexp_replace = '^\s+|\s+$|\.'

        for row in [tr.getchildren() for tr in first_league_table[1:]]:
            current_row = []
            first_td = re.sub('\s', '', row[0].text)
            if first_td == '.' or first_td == '':
                continue
            if first_division_index is not None:
                current_division_name = re.sub('\s', '', row[first_division_index].text)
                if first_division_name is None:
                    first_division_name = current_division_name
                elif current_division_name != first_division_name:
                    continue
            for property_index in properties_indecies:
                current_children = row[property_index].getchildren()
                if len(current_children) != 0:
                    current_row.append(re.sub(prop_regexp_replace, '', current_children[0].text))
                else:
                    current_row.append(re.sub(prop_regexp_replace, '', row[property_index].text))
            new_parsed_data.append(current_row)
        return new_parsed_data





