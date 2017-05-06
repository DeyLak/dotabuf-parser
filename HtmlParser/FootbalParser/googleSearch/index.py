from HtmlParser.FootbalParser.googleSearch.SearchPage import SearchPage

def run_teams_search():
    with open('./input.txt', "r") as f:
        teams = [team.replace('\n', '') for team in f.readlines()]
    parsed_names = {}
    result = []
    for team in teams:
        if team in parsed_names:
            current_team_name = parsed_names[team]
        else:
            current_team_name = SearchPage(team).parse()
            parsed_names[team] = current_team_name
        result.append(current_team_name)
    with open('./output.txt', "w") as f:
        for team in result:
            f.write('%s\n' % team)

if __name__ == '__main__':
    run_teams_search()