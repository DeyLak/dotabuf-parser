from dotabuffParser.DotabuffConnector import get_page
from dotabuffParser.DotabuffUrls import get_match_url
from dotabuffParser.HtmlParsingHelpers import get_table_row_names, parse_table_row


class MatchPage:
    def __init__(self, match_id):
        self.match_id = str(match_id)

    def parse(self):
        url = get_match_url(self.match_id)
        self.page = page = get_page(url)

        match_info_table = page.getroot().cssselect('section.radiant > article.r-tabbed-table > table')[0].getchildren()
        #getting necessary tr tag according to table structure
        col_names = get_table_row_names(match_info_table[0].getchildren()[0])
        for row in match_info_table[1].getchildren():
            current_row = parse_table_row(row, col_names)
            print(current_row)

