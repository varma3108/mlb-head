import requests
import time
from pprint import pp
from common_functions import replace_null_year_month_day, \
    print_time

def get_api_data(url: str) -> dict:
    print_time(f'fetching from {url}')
    time.sleep(2)
    headers = {"accept": "application/json"}
    response = requests.get(url, headers = headers)
    data = response.json()
    return data

# functions to get endpoints properly with f-strings
def get_api_endpoint_daily_summary(params: dict) -> str:
    # used to get games for a specific day
    # docs https://developer.sportradar.com/baseball/reference/mlb-daily-summary
    access_level = params['access_level']
    language_code = params['language_code']
    year, month, day = replace_null_year_month_day(params['year'], params['month'], params['day'])
    format = params['format']
    api_key = params['api_key']
    return f'https://api.sportradar.com/mlb/{access_level}/v7/{language_code}/games/{year}/{month}/{day}/summary.{format}?api_key={api_key}'

def get_api_endpoint_seasonal_standings(params: dict) -> str:
    # used to get streak for each team in the league
    # docs https://developer.sportradar.com/baseball/reference/mlb-standings
    access_level = params['access_level']
    language_code = params['language_code']
    format = params['format']
    api_key = params['api_key']
    season_year = params['season_year']
    season_type = params['season_type']
    return f'https://api.sportradar.com/mlb/{access_level}/v7/{language_code}/seasons/{season_year}/{season_type}/standings.{format}?api_key={api_key}'

def get_api_endpoint_seasonal_statistics(params: dict) -> str:
    # used to get obp and ops for each team
    # docs https://developer.sportradar.com/baseball/reference/mlb-seasonal-statistics
    access_level = params['access_level']
    language_code = params['language_code']
    format = params['format']
    api_key = params['api_key']
    season_year = params['season_year']
    season_type = params['season_type']
    team_id = params['team_id']
    # jason['statistics']['hitting']['overall']['obp']
    # jason['statistics']['hitting']['overall']['ops']
    return f'https://api.sportradar.com/mlb/{access_level}/v7/{language_code}/seasons/{season_year}/{season_type}/teams/{team_id}/statistics.{format}?api_key={api_key}'

def get_api_endpoint_todays_team_statistics(params: dict) -> str:
    year, month, day = replace_null_year_month_day(params['year'], params['month'], params['day'])
    effective_date = f'{year}-{month}-{day}'
    return f'https://bdfed.stitch.mlbinfra.com/bdfed/transform-mlb-standings?&splitPcts=false&numberPcts=false&standingsView=sport&sortTemplate=3&season=2024&leagueIds=103&&leagueIds=104&standingsTypes=regularSeason&contextTeamId=&date={effective_date}&hydrateAlias=noSchedule'

def get_api_endpoint_todays_games(params: dict) -> str:
    year, month, day = replace_null_year_month_day(params['year'], params['month'], params['day'])
    effective_date = f'{year}-{month}-{day}'
    return f'https://statsapi.mlb.com/api/v1/schedule?sportId=1&sportId=51&sportId=21&startDate={effective_date}&endDate={effective_date}&timeZone=America/New_York&gameType=E&&gameType=S&&gameType=R&&gameType=F&&gameType=D&&gameType=L&&gameType=W&&gameType=A&language=en&leagueId=104&&leagueId=103&&leagueId=160&&leagueId=590&sortBy=gameDate,gameType&hydrate=team,linescore(matchup,runners),xrefId,flags,statusFlags,broadcasts(all),venue(location),decisions,person,probablePitcher,stats,game(content(media(epg),summary),tickets),seriesStatus(useOverride=true)'


if __name__ == '__main__':
    pass