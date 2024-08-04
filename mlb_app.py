from flask import Flask, render_template, request, redirect, g, url_for
import datetime
import os
from bs4 import BeautifulSoup
from pprint import pp
import pandas as pd
from common_functions import print_df, \
    print_time, \
    infile_exists, \
    save_dataframe_to_csv, \
    read_csv_to_dataframe

from mlb_parse_functions import parse_daily_summary_data, \
    get_teams_from_daily_summary_df, \
    parse_seasonal_standings_data, \
    parse_seasonal_statistics_data

from mlb_orch_functions import orch_daily_summary_df, \
    orch_seasonal_standings, \
    orch_seasonal_statistics, \
    orch_historic_statistics, \
    orch_todays_team_statistics, \
    orch_todays_games

# import mlb_constants
from mlb_constants import shared_params, \
    api_params_daily_summary, \
    api_params_seasonal_standings, \
    api_params_seasonal_statistics, \
    api_endpoint_7d, \
    api_endpoint_15d, \
    api_endpoint_30d, \
    x_days_back_data, \
    api_params_todays_team_statistics, \
    api_params_todays_games, \
    html_table_select_columns, \
    rename_dict, \
    new_html_table_select_columns, \
    new_rename_dict

currentDirectory = os.path.dirname(os.path.abspath(__file__))
al_standings = pd.read_csv('/Users/srisatyaindukuri/Downloads/golden-picks-main 2/cache/AL-standings.csv')
nl_standings = pd.read_csv('/Users/srisatyaindukuri/Downloads/golden-picks-main 2/cache/NL-standings.csv')



app = Flask(__name__)

@app.route('/')
def index():
    author = 'Ben Godgart'
    return render_template('mlb_homepage.html', author=author)


@app.route('/fetch_mlb_data', methods=['POST'])
def fetch_mlb_data():
    order = ['historic_statistics',
             'todays_team_statistics']
    current_directory = os.path.dirname(os.path.abspath(__file__))
    todays_date = datetime.datetime.today().strftime('%Y-%m-%d')




    todays_games_download_filename = os.path.join(current_directory, 'static', f'raw_todays_games_download_{todays_date}.csv')
    todays_games_download_filename_raw_download = f'raw_todays_games_download_{todays_date}.csv'
    todays_report_filename = os.path.join(current_directory, 'static', f'todays_report_{todays_date}.csv')
    todays_report_filename_raw_download = f'todays_report_{todays_date}.csv'
    

    historic_statistics_filename = os.path.join(current_directory, 'static', f'raw_todays_historic_statistics_obp_ops_{todays_date}.csv')
    if infile_exists(historic_statistics_filename):
        historic_statistics_df = read_csv_to_dataframe(historic_statistics_filename)
    else:
        historic_statistics_df = orch_historic_statistics(x_days_back_data)
        save_dataframe_to_csv(historic_statistics_df, historic_statistics_filename)

    # old_version = False
    # if old_version: # old version for legacy processing with sportradar api
    #     daily_summary_filename = os.path.join(current_directory, 'static', f'raw_todays_daily_summary_games_{todays_date}.csv')
    #     if infile_exists(daily_summary_filename):
    #         daily_summary_df = read_csv_to_dataframe(daily_summary_filename)
    #     else:
    #         daily_summary_df = orch_daily_summary_df(api_params_daily_summary)
    #         save_dataframe_to_csv(daily_summary_df, daily_summary_filename)
    #     teams_playing_today = get_teams_from_daily_summary_df(daily_summary_df)
    #     # pp(teams_playing_today)

    #     seasonal_standings_filename = os.path.join(current_directory, 'static', f'raw_todays_seasonal_standings_{todays_date}.csv')
    #     if infile_exists(seasonal_standings_filename):
    #         seasonal_standings_df = read_csv_to_dataframe(seasonal_standings_filename)
    #     else:
    #         seasonal_standings_df = orch_seasonal_standings(api_params_seasonal_standings)
    #         save_dataframe_to_csv(seasonal_standings_df, seasonal_standings_filename)

    #     seasonal_statistics_filename = os.path.join(current_directory, 'static', f'raw_todays_statistics_{todays_date}.csv')
    #     if infile_exists(seasonal_statistics_filename):
    #         seasonal_statistics_df = read_csv_to_dataframe(seasonal_statistics_filename)
    #     else:
    #         seasonal_statistics_df = orch_seasonal_statistics(api_params_seasonal_statistics, teams_list = teams_playing_today)
    #         save_dataframe_to_csv(seasonal_statistics_df, seasonal_statistics_filename)

    #     print_time('merging...')
    #     teams_with_statistics = seasonal_statistics_df.merge(seasonal_standings_df, how = 'left', on = ['team_guid'])
    #     teams_with_historic_statistics = teams_with_statistics.merge(historic_statistics_df, on = ['team_abbr'])
    #     merged_df = daily_summary_df.merge(teams_with_historic_statistics, how = 'left', left_on = ['home_team_guid'], right_on = ['team_guid'])
    #     merged_df = merged_df.merge(teams_with_historic_statistics, how = 'left', left_on = ['away_team_guid'], right_on = ['team_guid'], suffixes = ['_home', '_away'])

    #     merged_df['spread'] = '0'
    #     merged_df['at'] = 'at'
    #     merged_df['matchup'] = merged_df['team_abbr_away'] + ' at ' + merged_df['team_abbr_home']
    #     # pp(merged_df.columns.tolist())

    #     save_dataframe_to_csv(merged_df, todays_games_download_filename)

    #     merged_df = read_csv_to_dataframe(todays_games_download_filename)
    #     # pp(merged_df.columns.tolist())
        
    #     merged_df = merged_df[html_table_select_columns]

    #     merged_df = merged_df.rename(columns = rename_dict)
    #     save_dataframe_to_csv(merged_df, todays_report_filename)


    #     merged_df_html = merged_df.to_html(index = False, header = False)
    #     soup = BeautifulSoup(merged_df_html, "html.parser")
    #     soup.find('table').unwrap()
    #     tbody_here = soup


    #     return redirect(url_for('mlb_table', tbody_here = tbody_here, report_data_url = f'/{todays_report_filename_raw_download}', raw_data_url = f'/{todays_games_download_filename_raw_download}'))
    
    # else: # new version
    
    todays_team_statistics_filename = os.path.join(current_directory, 'static', f'raw_todays_team_statistics_{todays_date}.csv')
    if infile_exists(todays_team_statistics_filename):
        todays_team_statistics_df = read_csv_to_dataframe(todays_team_statistics_filename)
    else:
        todays_team_statistics_df = orch_todays_team_statistics(api_params_todays_team_statistics)
        save_dataframe_to_csv(todays_team_statistics_df, todays_team_statistics_filename)
    
    todays_games_filename = os.path.join(current_directory, 'static', f'raw_todays_games_{todays_date}.csv')
    if infile_exists(todays_games_filename):
        todays_games_df = read_csv_to_dataframe(todays_games_filename)
    else:
        todays_games_df = orch_todays_games(api_params_todays_games)

    teams_historic_and_todays_stats = historic_statistics_df.merge(todays_team_statistics_df, how='inner', on='team_abbr')
    home_teams_merged = todays_games_df.merge(teams_historic_and_todays_stats, how = 'left', left_on = 'team_abbr_home', right_on = 'team_abbr')
    both_teams_merged = home_teams_merged.merge(teams_historic_and_todays_stats, how = 'left', left_on = 'team_abbr_away', right_on = 'team_abbr', suffixes = ['_hometeam', '_awayteam'])


    both_teams_merged['at'] = 'at'
    both_teams_merged['matchup'] = both_teams_merged['team_abbr_away'] + ' at ' + both_teams_merged['team_abbr_home']

    pp(both_teams_merged.columns.tolist())

    save_dataframe_to_csv(both_teams_merged, todays_games_download_filename)

    both_teams_merged = read_csv_to_dataframe(todays_games_download_filename)

    both_teams_merged = both_teams_merged[new_html_table_select_columns]
    # pp(both_teams_merged.columns.tolist())

    both_teams_merged = both_teams_merged.rename(columns = new_rename_dict)
    # pp(both_teams_merged.columns.tolist())

    both_teams_merged_html = both_teams_merged.to_html(index = False, header = False)
    soup = BeautifulSoup(both_teams_merged_html, "html.parser")
    soup.find('table').unwrap()
    tbody_here = soup

    # print_df(both_teams_merged)
    save_dataframe_to_csv(both_teams_merged, todays_report_filename)
    
    # return redirect('/')
    return redirect(url_for('mlb_table_new', tbody_here = tbody_here, report_data_url = f'/{todays_report_filename_raw_download}', raw_data_url = f'/{todays_games_download_filename_raw_download}'))

@app.route('/mlb_table')
def mlb_table():
    tbody_here = request.args.get('tbody_here')
    report_data_url = request.args.get('report_data_url')
    raw_data_url = request.args.get('raw_data_url')
    return render_template('mlb_table.html', tbody_here = tbody_here, report_data_url = url_for('static', filename = report_data_url), raw_data_url = url_for('static', filename = raw_data_url))

@app.route('/mlb_table_new')
def mlb_table_new():
    tbody_here = request.args.get('tbody_here')
    report_data_url = request.args.get('report_data_url')
    raw_data_url = request.args.get('raw_data_url')
    return render_template('mlb_table_new.html', tbody_here = tbody_here, report_data_url = url_for('static', filename = report_data_url), raw_data_url = url_for('static', filename = raw_data_url))

@app.route('/al_standings')
def show_al_standings():
    return render_template('al_standings.html', tables=[al_standings.to_html(classes='data')], titles=al_standings.columns.values)

@app.route('/nl_standings')
def show_nl_standings():
    return render_template('nl_standings.html', tables=[nl_standings.to_html(classes='data')], titles=nl_standings.columns.values)



if __name__ == '__main__':
    #app.run(host='0.0.0.0')
    app.run(port=5001, debug=True)