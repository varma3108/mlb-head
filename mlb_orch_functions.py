
from pprint import pp
import pandas as pd
from common_functions import print_time, \
    format_1z3_addleadingzero, \
    format_1z3_addtrailingzeros
from mlb_api_functions import get_api_data, \
    get_api_endpoint_daily_summary, \
    get_api_endpoint_seasonal_standings, \
    get_api_endpoint_seasonal_statistics, \
    get_api_endpoint_todays_team_statistics, \
    get_api_endpoint_todays_games
from mlb_parse_functions import parse_daily_summary_data, \
    parse_seasonal_standings_data, \
    parse_seasonal_statistics_data, \
    parse_historic_data, \
    parse_todays_team_statistics_data, \
    parse_todays_games_data
import mlb_constants


def orch_daily_summary_df(api_params_daily_summary: dict) -> pd.DataFrame:
    daily_summary_api_endpoint = get_api_endpoint_daily_summary(api_params_daily_summary)
    daily_summary_data = get_api_data(daily_summary_api_endpoint)
    daily_summary_df = parse_daily_summary_data(daily_summary_data).sort_values(['game_time_est']).reset_index(drop = True)
    return daily_summary_df

def orch_seasonal_standings(api_params_seasonal_standings: dict) -> pd.DataFrame:
    standings_api_endpoint = get_api_endpoint_seasonal_standings(api_params_seasonal_standings)
    seasonal_standings_data = get_api_data(standings_api_endpoint)
    seasonal_standings_df = parse_seasonal_standings_data(seasonal_standings_data)
    return seasonal_standings_df

def orch_seasonal_statistics(api_params_seasonal_statistics: dict, teams_list:list) -> pd.DataFrame:
    all_team_statistics = []
    for idx, team in enumerate(teams_list):
        print_time(f'processing team {idx + 1} of {len(teams_list)}')
        api_params_seasonal_statistics['team_id'] = team
        statistics_api_endpoint = get_api_endpoint_seasonal_statistics(api_params_seasonal_statistics)
        statistics_data = get_api_data(statistics_api_endpoint)
        team_statistics = parse_seasonal_statistics_data(statistics_data) # this is a dict (row)
        # pp(team_statistics)
        all_team_statistics.append(team_statistics)
    # pp(all_team_statistics)
    print_time('dataframing')
    seasonal_statistics_df = pd.DataFrame.from_records(all_team_statistics)
    # seasonal_statistics_df['team_run_diff'] = seasonal_statistics_df['team_runs_scored_total'].astype(int) - seasonal_statistics_df['team_runs_allowed_total'].astype(int)
    seasonal_statistics_df = format_1z3_addtrailingzeros(seasonal_statistics_df, ['team_obp', 'team_ops'])

    return seasonal_statistics_df


def orch_historic_statistics(x_days_back_data: dict) -> pd.DataFrame:
    def loop_historic_teams_statistics(x_days_back_data: dict) -> list:
        xdb_dfs = []
        for xdb in x_days_back_data:
            params = x_days_back_data[xdb]
            num_days = params['num_days']
            api_endpoint = params['api_endpoint']
            data = get_api_data(api_endpoint)
            teams_df = parse_historic_data(data, num_days)
            xdb_dfs.append(teams_df)
        return xdb_dfs

    def merge_historic_dfs(xdb_dfs: list) -> pd.DataFrame:
        base_df = None
        for idx, df in enumerate(xdb_dfs):
            if idx == 0:
                base_df = df 
                continue
            else:
                base_df = base_df.merge(df, how = 'left', on = ['team_abbr'])

        # print_time(base_df.columns.to_list())
        return base_df

    xdb_dfs = loop_historic_teams_statistics(x_days_back_data)
    historic_statistics_df = merge_historic_dfs(xdb_dfs)
    return historic_statistics_df


def orch_todays_team_statistics(api_params_todays_teams: dict) -> pd.DataFrame:
    todays_team_statistics_endpoint = get_api_endpoint_todays_team_statistics(api_params_todays_teams)
    todays_team_statistics_data = get_api_data(todays_team_statistics_endpoint)
    todays_team_statistics_df = parse_todays_team_statistics_data(todays_team_statistics_data)
    return todays_team_statistics_df

def orch_todays_games(api_params_todays_games: dict) -> pd.DataFrame:
    todays_games_endpoint = get_api_endpoint_todays_games(api_params_todays_games)
    todays_games_data = get_api_data(todays_games_endpoint)
    todays_games_df = parse_todays_games_data(todays_games_data)
    return todays_games_df

if __name__ == '__main__':
    pass