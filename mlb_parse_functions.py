import datetime
import pandas as pd
from pprint import pp
import pytz
import time
from common_functions import replace_null_year_month_day, \
    print_df, \
    print_time, \
    format_1z3_addleadingzero, \
    format_1z3_addtrailingzeros, \
    save_dataframe_to_csv, \
    read_csv_to_dataframe, \
    infile_exists



# functions to parse current data from sportradar api
def parse_daily_summary_data(data: dict) -> pd.DataFrame:
    # this is what returns the list of games
    games_to_return = []
    games = data['league']['games'] # list of games
    for idx, game_data in enumerate(games):
        print_time(f'game {idx + 1} of {len(games)}')
        game = game_data['game']
        game_time_utc = game['scheduled']
        game_time_dt = datetime.datetime.fromisoformat(game_time_utc)
        game_time_est = game_time_dt.astimezone(pytz.timezone('US/Eastern'))
        game_time_est_readable = game_time_est.strftime(r'%a %m-%d-%Y at %I:%M %p EST')
        home_team = game['home']
        # home_team_abbr = home_team['abbr']
        home_team_id = home_team['id']
        away_team = game['away']
        # away_team_abbr = away_team['abbr']
        away_team_id = away_team['id']
        game_row = {
            'game_time_utc': game_time_utc,
            'game_time_dt': game_time_dt,
            'game_time_est': game_time_est,
            'game_time_est_readable': game_time_est_readable,
            # 'home_team_abbr': home_team_abbr,
            'home_team_guid': home_team_id, 
            # 'away_team_abbr': away_team_abbr
            'away_team_guid': away_team_id
        }
        # games_to_return.append(copy.deepcopy(game_row))
        games_to_return.append(game_row)
    print_time('dataframing')
    games_df = pd.DataFrame.from_records(data = games_to_return)
    return games_df

def get_teams_from_daily_summary_df(daily_summary_df: pd.DataFrame) -> list:
    home_teams = daily_summary_df['home_team_guid'].to_list()
    away_teams = daily_summary_df['away_team_guid'].to_list()
    teams_list = list(set(home_teams + away_teams))
    return teams_list

def parse_seasonal_standings_data(data: dict) -> pd.DataFrame:
    # this is what returns statistics for each team including team info
    teams_to_return = []
    team_season_guid = data['league']['season']['id']
    try: 
        leagues = data['league']['season']['leagues']
    except KeyError:
        time.sleep(3)
        leagues = data['league']['season']['leagues']
    team_season_guid = data['league']['season']['id']

    for league in leagues:
        league_name = league['name']
        league_abbr = league['alias']
        divisions = league['divisions']
        for division in divisions:
            division_name = division['name']
            division_abbr = division['alias']
            teams = division['teams']
            for idx, team in enumerate(teams):
                print_time(f'team {idx + 1} of {len(teams)} in {league_name} {division_name}')
                team_name = team['name']
                team_market = team['market']
                team_abbr = team['abbr']
                team_id = team['id']
                team_streak = team['streak']
                team_loss = team['loss']
                team_win = team['win']
                team_win_pct = team['win_p']
                team_league_rank = team['rank']['league']
                team_division_rank = team['rank']['division']
                team_away_loss = team['away_loss']
                team_away_win = team['away_win']
                team_home_loss = team['home_loss']
                team_home_win = team['home_win']
                team_last_10_lost = team['last_10_lost']
                team_last_10_won = team['last_10_won']
                # possible additional statistics to pull per team
                    # games_back
                    # away_loss 
                    # away_win
                    # home_loss
                    # home_win
                    # last_10_lost
                    # last_10_won
                team_row = {
                    'team_name': team_name,
                    'team_market': team_market,
                    'team_abbr': team_abbr,
                    'team_guid': team_id,
                    'team_season_guid': team_season_guid,
                    'team_streak': team_streak,
                    'team_loss': team_loss,
                    'team_win': team_win,
                    'team_win_pct': team_win_pct,
                    'team_league': league_name,
                    'team_league_abbr': league_abbr,
                    'team_league_rank': team_league_rank,
                    'team_division_name': division_name,
                    'team_division_abbr': division_abbr,
                    'team_division_rank': team_division_rank,
                    'team_away_loss': team_away_loss,
                    'team_away_win': team_away_win,
                    'team_home_loss': team_home_loss,
                    'team_home_win': team_home_win,
                    'team_last_10_lost': team_last_10_lost,
                    'team_last_10_won': team_last_10_won
                }
                teams_to_return.append(team_row)
    print_time('dataframing')
    teams_df = pd.DataFrame.from_records(teams_to_return)
    teams_df['team_longname'] = teams_df['team_market'] + ' ' + teams_df['team_name']
    # teams_df['team_wr_streak'] = teams_df['team_win_pct'].astype(str) + ' ' + teams_df['team_streak']
    teams_df['team_league_division'] = teams_df['team_league_abbr'] + ' ' + teams_df['team_division_abbr']
    teams_df['team_league_division_ranks'] = teams_df['team_league_rank'].astype(str) + ' ' + teams_df['team_division_rank'].astype(str)
    teams_df['team_home_win_pct'] = round(teams_df['team_home_win'].astype(float) / (teams_df['team_home_win'].astype(float) + teams_df['team_home_loss'].astype(float)), 3)
    teams_df['team_away_win_pct'] = round(teams_df['team_away_win'].astype(float) / (teams_df['team_away_win'].astype(float) + teams_df['team_away_loss'].astype(float)), 3)
    teams_df['team_last_10_win_pct'] = round(teams_df['team_last_10_won'].astype(float) / (teams_df['team_last_10_won'].astype(float) + teams_df['team_last_10_lost']), 3)
    teams_df = format_1z3_addtrailingzeros(teams_df, ['team_win_pct', 'team_home_win_pct', 'team_away_win_pct', 'team_last_10_win_pct'])
    
    return teams_df
    
def parse_seasonal_statistics_data(data: dict) -> dict:
    # used for getting obp and ops but there are lots of other statistics we can pull from this
    if 'message' in list(data.keys()):
        pp(data['message'])
        print_time('did you send too many requests too fast? add a delay before repeated requests!')
    team_statistics = {}
    team_guid = data['id']
    team_season = data['season']['id']
    team_obp = data['statistics']['hitting']['overall']['obp']
    team_ops = data['statistics']['hitting']['overall']['ops']
    # team_runs_scored_total = data['statistics']['hitting']['overall']['runs']['total']
    # team_runs_allowed_total = data['statistics']['pitching']['overall']['runs']['total']

    team_statistics = {
        'team_guid': team_guid,
        'team_season': team_season,
        'team_obp': team_obp,
        'team_ops': team_ops
        # 'team_runs_scored_total': team_runs_scored_total,
        # 'team_tuns_allowed_total': team_runs_allowed_total
    }
    print_time('returning team statistics as dict (row)')
    return team_statistics


# functions to parse historic data
def parse_historic_data(data: dict, num_days: int) -> pd.DataFrame:
    days_id = '_' + str(num_days) + 'd'
    teams_to_return = []
    teams = data['stats']
    for team in teams:
        team_abbr = team['teamAbbrev']
        team_obp = team['obp']
        team_ops = team['ops']
        team_row = {
            'team_abbr': team_abbr,
            'team_obp' + days_id: team_obp,
            'team_ops' + days_id: team_ops,
        }
        teams_to_return.append(team_row)
    print_time('dataframing')
    historic_statistics_df = pd.DataFrame.from_records(teams_to_return)
    historic_statistics_df = format_1z3_addleadingzero(historic_statistics_df, ['team_obp' + days_id, 'team_ops' + days_id])
    # print_time(historic_statistics_df.columns.to_list())
    historic_statistics_df = add_ranking_cols(historic_statistics_df, ['team_obp' + days_id, 'team_ops' + days_id])
    return historic_statistics_df

def add_ranking_cols(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    for col in cols:
        df[col + '_rank'] = df[col].rank(method='max', ascending=False).astype(int)
    # print_time(df.columns.to_list())
    return df

def parse_todays_team_statistics_data(data: dict) -> pd.DataFrame:
    teams_to_return = []
    team_records = data['records'][0]['teamRecords']
    for team in team_records: 
        team_row = {}
        team_row['team_abbr'] = team['abbreviation']
        team_row['team_wins'] = team['wins']
        team_row['team_losses'] = team['losses']
        team_row['team_win_pct'] = team['pct']
        team_row['team_runs_allowed'] = team['runsAllowed']
        team_row['team_runs_scored'] = team['runsScored']
        team_row['team_run_diff'] = team['runDifferential']
        team_row['team_streak'] = team['streak']
        team_row['team_record_last_ten'] = team['record_lastTen']
        team_row['team_last_10_wins'], team_row['team_last_10_losses'] = team_row['team_record_last_ten'].split('-')
        team_row['team_last_10_win_pct'] = round(float(int(team_row['team_last_10_wins'])/(int(team_row['team_last_10_wins'])+int(team_row['team_last_10_losses']))), 3)
        team_row['team_record_home'] = team['record_home']
        team_row['team_home_wins'], team_row['team_home_losses'] = team_row['team_record_home'].split('-')
        team_row['team_home_win_pct'] = round(float(int(team_row['team_home_wins'])/(int(team_row['team_home_wins'])+int(team_row['team_home_losses']))), 3)
        team_row['team_record_away'] = team['record_away']
        team_row['team_away_wins'], team_row['team_away_losses'] = team_row['team_record_away'].split('-')
        team_row['team_away_win_pct'] = round(float(int(team_row['team_away_wins'])/(int(team_row['team_away_wins'])+int(team_row['team_away_losses']))), 3)
        teams_to_return.append(team_row)
    print('dataframing')
    teams_df = pd.DataFrame.from_records(teams_to_return)
    print(teams_df.columns.to_list())
    return teams_df

# functions to parse todays games data
def parse_todays_games_data(data: dict) -> pd.DataFrame:
    games_to_return = []
    dates = data['dates']
    today = datetime.datetime.today().date().strftime('%Y-%m-%d') # '2024-06-19'
    for idx, game_date in enumerate(dates):
        if game_date['date'] == today:
            todays_games = dates[idx]['games']
            break
        else:
            print('not this date!')
    for game in todays_games:
        game_row = {}
        game_row['game_date'] = game['gameDate']
        print_time(game_row['game_date'])
        game_time_dt = datetime.datetime.fromisoformat(game_row['game_date'])
        game_time_est = game_time_dt.astimezone(pytz.timezone('US/Eastern'))
        game_row['game_time_est_readable'] = game_time_est.strftime(r'%a %m-%d-%Y at %I:%M %p EST')
        game_row['team_abbr_away'] = game['teams']['away']['team']['abbreviation']
        game_row['team_abbr_home'] = game['teams']['home']['team']['abbreviation']
        game_row['series_games_total'] = game['gamesInSeries']
        game_row['series_game_number'] = game['seriesGameNumber']
        games_to_return.append(game_row)
    print('dataframing')
    games_df = pd.DataFrame.from_records(games_to_return)
    print(games_df.columns.to_list())
    return games_df



if __name__ == '__main__':
    pass