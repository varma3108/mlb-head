# api params for sportradar api calls for current data

# sportradar api key for trial requests
# api_key = '7bVD3Dwgyq3a3jBH4eYW1alfyMMEdheq9Iq15q0E'
api_key = 'CntE3gVvdG5KhgQLejzu387v8Uv4tU3Y588l33A3'

shared_params = {
    'api_key': api_key,
    'access_level': 'trial',
    'language_code': 'en',
    'format': 'json',
    'year': None,
    'month': None,
    'day': None,
    'season_year': '2024',
    'reg_or_pre': 'REG'
}

api_params_daily_summary = {
    'api_key': shared_params['api_key'],
    'access_level': shared_params['access_level'],
    'language_code': shared_params['language_code'],
    'format': shared_params['format'],
    'year': shared_params['year'],
    'month': shared_params['month'],
    'day': shared_params['day']
}

api_params_seasonal_standings = {
    'api_key': shared_params['api_key'],
    'access_level': shared_params['access_level'],
    'language_code': shared_params['language_code'],
    'format': shared_params['format'],
    'season_year': shared_params['season_year'],
    'season_type': shared_params['reg_or_pre']
}

api_params_seasonal_statistics = {
    'api_key': shared_params['api_key'],
    'access_level': shared_params['access_level'],
    'language_code': shared_params['language_code'],
    'format': shared_params['format'],
    'season_year': shared_params['season_year'],
    'season_type': shared_params['reg_or_pre'],
    'team_id': ''
}


api_params_todays_team_statistics = {
    'year': shared_params['year'],
    'month': shared_params['month'],
    'day': shared_params['day'],
    'season_year': shared_params['season_year'],
    'reg_or_pre': shared_params['reg_or_pre'],
    'timezone':'America/New_York'
}

api_params_todays_teams = {
    'year': shared_params['year'],
    'month': shared_params['month'],
    'day': shared_params['day'],
    'season_year': shared_params['season_year'],
    'reg_or_pre': shared_params['reg_or_pre'],
    'timezone':'America/New_York'}

api_params_todays_games = {
    'year': shared_params['year'],
    'month': shared_params['month'],
    'day': shared_params['day'],
    'season_year': shared_params['season_year'],
    'reg_or_pre': shared_params['reg_or_pre'],
    'timezone':'America/New_York'
}

# api endpoints and params for api calls for historic data
api_endpoint_7d = 'https://bdfed.stitch.mlbinfra.com/bdfed/stats/team?&env=prod&sportId=1&startDate=2024-06-07&gameType=R&group=hitting&order=desc&sortStat=gamesPlayed&stats=season&season=2024&limit=30&offset=0&daysBack=-6'
api_endpoint_15d = 'https://bdfed.stitch.mlbinfra.com/bdfed/stats/team?&env=prod&sportId=1&gameType=R&group=hitting&order=desc&sortStat=gamesPlayed&stats=season&season=2024&limit=30&offset=0&daysBack=-14'
api_endpoint_30d = 'https://bdfed.stitch.mlbinfra.com/bdfed/stats/team?&env=prod&sportId=1&gameType=R&group=hitting&order=desc&sortStat=gamesPlayed&stats=season&season=2024&limit=30&offset=0&daysBack=-29'

x_days_back_data = {
    '7d': {'num_days': 7, 'api_endpoint': api_endpoint_7d}, 
    '15d': {'num_days': 15, 'api_endpoint': api_endpoint_15d}, 
    '30d': {'num_days': 30, 'api_endpoint': api_endpoint_30d}
}

html_table_select_columns = [
    'matchup',
    'game_time_est_readable', 
    'team_ops_30d_rank_away',
    'team_ops_15d_rank_away',
    'team_ops_7d_rank_away',
    'team_obp_30d_rank_away',
    'team_obp_15d_rank_away',
    'team_obp_7d_rank_away',
    'team_win_pct_away', 
    # 'team_last_10_win_pct_away',
    'team_streak_away',
    # 'team_run_diff_away',
    'team_abbr_away',
    'spread',
    'at',
    'team_abbr_home',
    'team_win_pct_home', 
    # 'team_last_10_win_pct',
    'team_streak_home',
    # 'team_run_diff_home',
    'team_obp_30d_rank_home',
    'team_obp_15d_rank_home',
    'team_obp_7d_rank_home',
    'team_ops_30d_rank_home',
    'team_ops_15d_rank_home',
    'team_ops_7d_rank_home'


    # 'team_longname_home', 
    # 'team_wr_streak_home',
    # 'team_longname_away', 
    # 'team_wr_streak_away',
    # 'team_obp_home',
    # 'team_ops_home',
    # 'team_obp_away',
    # 'team_ops_away',
    # 'team_league_abbr_home',
    # 'team_division_abbr_home',
    # 'team_league_division_home',
    # 'team_league_rank_home',
    # 'team_division_rank_home',
    # 'team_league_division_ranks_home',
    # 'team_league_abbr_away',
    # 'team_division_abbr_away', 
    # 'team_league_division_away',
    # 'team_league_rank_away', 
    # 'team_division_rank_away',
    # 'team_league_division_ranks_away',
    # 'team_obp_7d_home',
    # 'team_ops_7d_home',
    # 'team_obp_15d_home',
    # 'team_ops_15d_home',
    # 'team_obp_30d_home',
    # 'team_ops_30d_home',
    # 'team_obp_7d_away',
    # 'team_ops_7d_away',
    # 'team_obp_15d_away',
    # 'team_ops_15d_away',
    # 'team_obp_30d_away',
    # 'team_ops_30d_away',
    ]

new_html_table_select_columns = [
    'matchup',
    'game_time_est_readable',
    # 'game_date',
    'series_game_number',
    'series_games_total',
    # 'team_abbr_away',
    'team_ops_30d_rank_awayteam',
    'team_ops_15d_rank_awayteam',
    'team_ops_7d_rank_awayteam',
    'team_obp_30d_rank_awayteam',
    'team_obp_15d_rank_awayteam',
    'team_obp_7d_rank_awayteam',

    'team_win_pct_awayteam',
    'team_away_win_pct_awayteam',
    'team_run_diff_awayteam',
    'team_streak_awayteam',
    'team_record_last_ten_awayteam',

    # 'team_obp_7d_awayteam',
    # 'team_ops_7d_awayteam',
    # 'team_obp_15d_awayteam',
    # 'team_ops_15d_awayteam',
    # 'team_obp_30d_awayteam',
    # 'team_ops_30d_awayteam',
    # 'team_wins_awayteam',
    # 'team_losses_awayteam',
    # 'team_runs_allowed_awayteam',
    # 'team_runs_scored_awayteam',
    # 'team_last_10_wins_awayteam',
    # 'team_last_10_losses_awayteam',
    # 'team_last_10_win_pct_awayteam',
    # 'team_record_home_awayteam',
    # 'team_home_wins_awayteam',
    # 'team_home_losses_awayteam',
    # 'team_home_win_pct_awayteam',
    # 'team_record_away_awayteam',
    # 'team_away_wins_awayteam',
    # 'team_away_losses_awayteam',
    'team_abbr_awayteam',

    'at',

    'team_abbr_hometeam',

    'team_win_pct_hometeam',
    'team_home_win_pct_hometeam',
    'team_run_diff_hometeam',
    'team_streak_hometeam',
    'team_record_last_ten_hometeam',

    'team_ops_30d_rank_hometeam',
    'team_ops_15d_rank_hometeam',
    'team_ops_7d_rank_hometeam',
    'team_obp_30d_rank_hometeam',
    'team_obp_15d_rank_hometeam',
    'team_obp_7d_rank_hometeam',

    # 'team_abbr_home',
    # 'team_obp_7d_hometeam',
    # 'team_ops_7d_hometeam',
    # 'team_obp_15d_hometeam',
    # 'team_ops_15d_hometeam',
    # 'team_obp_30d_hometeam',
    # 'team_ops_30d_hometeam',
    # 'team_wins_hometeam',
    # 'team_losses_hometeam',
    # 'team_runs_allowed_hometeam',
    # 'team_runs_scored_hometeam',
    # 'team_last_10_wins_hometeam',
    # 'team_last_10_losses_hometeam',
    # 'team_last_10_win_pct_hometeam',
    # 'team_record_home_hometeam',
    # 'team_home_wins_hometeam',
    # 'team_home_losses_hometeam',
    # 'team_record_away_hometeam',
    # 'team_away_wins_hometeam',
    # 'team_away_losses_hometeam',
    # 'team_away_win_pct_hometeam'
]

rename_dict = {
        'game_time_est_readable': 'game time',
        'team_longname_home': 'home team',
        'team_abbr_home': 'home',
        'team_win_pct_home': 'home win%',
        'team_streak_home': 'home streak',
        'team_wr_streak_home': 'home wr streak',
        'team_longname_away': 'away team',
        'team_abbr_away': 'away',
        'team_win_pct_away': 'away win%',
        'team_streak_away': 'away streak',
        'team_wr_streak_away': 'away wr streak',
        'team_obp_home': 'home obp',
        'team_ops_home': 'home ops',
        'team_obp_away': 'home obp',
        'team_ops_away': 'home ops',
        'team_league_abbr_home': 'home league',
        'team_division_abbr_home': 'home div',
        'team_league_division_home': 'home league div',
        'team_league_rank_home': 'home league rank',
        'team_division_rank_home': 'home div rank',
        'team_league_division_ranks_home': 'home ranks',
        'team_league_abbr_away': 'away league',
        'team_division_abbr_away': 'away div',
        'team_league_division_away': 'away league div',
        'team_league_rank_away': 'away league rank',
        'team_division_rank_away': 'away div rank',
        'team_league_division_ranks_away': 'away ranks',
        'team_obp_7d_home': 'home obp 7d raw',
        'team_ops_7d_home': 'home ops 7d raw',
        'team_obp_7d_rank_home': 'home obp 7d',
        'team_ops_7d_rank_home': 'home ops 7d',
        'team_obp_15d_home': 'home obp 15d raw',
        'team_ops_15d_home': 'home ops 15d raw',
        'team_obp_15d_rank_home': 'home obp 15d',
        'team_ops_15d_rank_home': 'home ops 15d',
        'team_obp_30d_home': 'home obp 30d raw',
        'team_ops_30d_home': 'home ops 30d raw',
        'team_obp_30d_rank_home': 'home obp 30d',
        'team_ops_30d_rank_home': 'home ops 30d',
        'team_obp_7d_away': 'away obp 7d raw',
        'team_ops_7d_away': 'away ops 7d raw',
        'team_obp_7d_rank_away': 'away obp 7d',
        'team_ops_7d_rank_away': 'away ops 7d',
        'team_obp_15d_away': 'away obp 15d raw',
        'team_ops_15d_away': 'away ops 15d raw',
        'team_obp_15d_rank_away': 'away obp 15d',
        'team_ops_15d_rank_away': 'away ops 15d',
        'team_obp_30d_away': 'away obp 30d raw',
        'team_ops_30d_away': 'away ops 30d raw',
        'team_obp_30d_rank_away': 'away obp 30d',
        'team_ops_30d_rank_away': 'away ops 30d',
        # 'team_last_10_win_pct_home': 'home last10 win%',
        # 'team_last_10_win_pct_away': 'away last10 win%'
    }

new_rename_dict = {
    'matchup': 'Matchup',
    'game_time_est_readable': 'Game Time',
    'series_game_number': 'Series Current Game Number',
    'series_games_total': 'Series Total Games',
    'team_ops_30d_rank_awayteam': 'Away Team 30d OPS Rank',
    'team_ops_15d_rank_awayteam': 'Away Team 15d OPS Rank',
    'team_ops_7d_rank_awayteam': 'Away Team 7d OPS Rank',
    'team_obp_30d_rank_awayteam': 'Away Team 30d OBP Rank',
    'team_obp_15d_rank_awayteam': 'Away Team 15d OBP Rank',
    'team_obp_7d_rank_awayteam': 'Away Team 7d OBP Rank',
    'team_win_pct_awayteam': 'Away Team Overall Win Percent',
    'team_away_win_pct_awayteam': 'Away Team Win Percent When Away',
    'team_run_diff_awayteam': 'Away Team Run Differential',
    'team_streak_awayteam': 'Away Team Streak',
    'team_record_last_ten_awayteam': 'Away Team Last 10 Record',
    'team_abbr_awayteam': 'Away Team Abbreviation',

    'at': 'At',

    'team_abbr_hometeam': 'Home Team Abbreviation',

    'team_win_pct_hometeam': 'Home Team Overall Win Percent',
    'team_home_win_pct_hometeam': 'Home Team Win Percent When Home',
    'team_run_diff_hometeam': 'Home Team Run Differential',
    'team_streak_hometeam': 'Home Team Streak',
    'team_record_last_ten_hometeam': 'Home Team Last 10 Record',

    'team_ops_30d_rank_hometeam': 'Home Team 30d OPS Rank',
    'team_ops_15d_rank_hometeam': 'Home Team 15d OPS Rank',
    'team_ops_7d_rank_hometeam': 'Home Team 7d OPS Rank',
    'team_obp_30d_rank_hometeam': 'Home Team 30d OBP Rank',
    'team_obp_15d_rank_hometeam': 'Home Team 15d OBP Rank',
    'team_obp_7d_rank_hometeam': 'Home Team 7d OBP Rank',
}
if __name__ == '__main__':
    pass    