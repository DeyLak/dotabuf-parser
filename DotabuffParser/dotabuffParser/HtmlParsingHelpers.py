from dotabuffParser.DotubuffParsingConstants import *


THOUSAND_SIGN = 'k'
NO_NUMBER_VALUE = '-'
def convert_to_number(string_number):
    if THOUSAND_SIGN in string_number:
        return int(float(string_number.replace(THOUSAND_SIGN, '')) * 1000)
    elif string_number != NO_NUMBER_VALUE:
        return int(string_number)
    return string_number

def get_table_row_names(tr_element):
    result = []
    for element in tr_element.getchildren():
        children = element.getchildren()
        if element.text is not None:
            result.append(element.text)
        elif len(children) > 0:
            result.append(children[0].text)
        else:
            result.append(None)

    return result

def parse_simple_text(item):
    if item.text is not None:
        return item.text
    return item.getchildren()[0].text

def parse_simple_number(item):
    return convert_to_number(parse_simple_text(item))

PARSING_FUNCTIONS = {
    HERO: lambda item: item.getchildren()[0].getchildren()[0].getchildren()[0].get('title'),
    KILLS: parse_simple_number,
    DEATHS: parse_simple_number,
    ASSISTS: parse_simple_number,
    NET_WORTH: parse_simple_number,
    LAST_HITS: parse_simple_number,
    DENIES: parse_simple_number,
    GPM: parse_simple_number,
    XPM: parse_simple_number,
    DAMAGE: parse_simple_number,
    HEAL: lambda item: parse_simple_number(item.getchildren()[0]),
    BUILDING_DAMAGE: parse_simple_number,
    WARDS_PLACED: lambda item: parse_simple_text(item.getchildren()[0]) + '/' + parse_simple_text(item.getchildren()[2]),
}

def parse_table_row(tr_element, col_names):
    result = []
    for i, element in enumerate(tr_element.getchildren()):
        current_column = col_names[i]
        if current_column in PARSING_FUNCTIONS:
            result.append(PARSING_FUNCTIONS[current_column](element))
        else:
            result.append(None)

    return result
