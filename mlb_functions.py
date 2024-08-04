import datetime
import glob
import pandas as pd
import time
from bs4 import BeautifulSoup
from pprint import pp
from common_functions import replace_null_year_month_day, \
    print_df, \
    print_time, \
    format_1z3_addleadingzero, \
    format_1z3_addtrailingzeros, \
    save_dataframe_to_csv, \
    read_csv_to_dataframe, \
    infile_exists
from mlb_api_functions import get_api_data, \
    get_api_endpoint_daily_summary, \
    get_api_endpoint_seasonal_standings, \
    get_api_endpoint_seasonal_statistics, \
    get_api_endpoint_todays_team_statistics, \
    get_api_endpoint_todays_games
    

import mlb_constants


# functions to parse todays team statistics data and orchestrate api calls




if __name__ == '__main__':
    pass