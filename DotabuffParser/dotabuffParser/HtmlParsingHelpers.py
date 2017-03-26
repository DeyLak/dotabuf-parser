from dotabuffParser.DotubuffParsingConstants import *


THOUSAND_SIGN = 'k'
NO_NUMBER_VALUE = '-'
def convert_to_number(string_number):
    if THOUSAND_SIGN in string_number:
        return int(float(string_number.replace(THOUSAND_SIGN, '')) * 1000)
    elif string_number != NO_NUMBER_VALUE:
        return int(string_number)
    return 0

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
    lastItem = item
    while lastItem.text is None:
        lastItem = lastItem.getchildren()[0]
    return lastItem.text

def parse_simple_number(item):
    text_number = parse_simple_text(item)
    if (text_number is None):
        return  0
    return convert_to_number(text_number)

def get_wards_object(obs, sentry):
    return {
        OBSERVER: obs,
        SENTRY: sentry,
    }

def parse_player(item):
    children = item.getchildren()
    if children[0].get('href') == '/players':
        return parse_simple_text(children[1])
    return parse_simple_text(children[0])

def parse_tooltip(item):
    return item.getchildren()[0].get('title')

PARSING_FUNCTIONS = {
    HERO: lambda item: item.getchildren()[0].getchildren()[0].getchildren()[0].get('title'),
    ROLE: parse_tooltip,
    LINE: parse_tooltip,
    PLAYER: parse_player,
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
    WARDS_PLACED: lambda item: get_wards_object(parse_simple_number(item.getchildren()[0]), parse_simple_number(item.getchildren()[2])),
}

def parse_table_row(tr_element, col_names):
    result = {}
    for i, element in enumerate(tr_element.getchildren()):
        current_column = col_names[i]
        if current_column in PARSING_FUNCTIONS:
            column_result = PARSING_FUNCTIONS[current_column](element)
            if (type(column_result) is dict):
                for key, value in column_result.items():
                    result[key] = value
            else:
                result[current_column] = column_result
    return result
