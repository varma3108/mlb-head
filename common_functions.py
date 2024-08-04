import datetime
import glob
import pandas as pd
import time
from pprint import pp

# helper functions
def replace_null_year_month_day(year, month, day):
    import datetime
    if not (year and month and day):
        
        today = datetime.datetime.today()
        print_time(f'No full date provided. Using today ({str(today)}) instead.')
        year = today.year
        month = today.month
        day = today.day
    return year, month, day

def print_df(df: pd.DataFrame):
    import pandas as pd
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
        print(df)
    return None

def print_time(message: str) -> None:
    import time
    print(f'{time.asctime()} -> {message}')
    return None

def format_1z3_addleadingzero(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    from pprint import pp
    # pp(df.columns.to_list())
    for col in cols:
        # print_time(f'col = {col}')
        df[col] = df[col].astype(str).str.rjust(5, '0')
    return df

def format_1z3_addtrailingzeros(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    import pandas as pd
    # pp(df.columns.to_list())
    for col in cols:
        # print_time(f'col = {col}')
        df[col] = df[col].astype(str).str.ljust(5, '0')
    return df

def save_dataframe_to_csv(df: pd.DataFrame, filename: str):
    import pandas as pd
    print_time(f'saving df to file {filename}')
    df.to_csv(filename, index=False)
    return None

def read_csv_to_dataframe(filename: str) -> pd.DataFrame:
    import pandas as pd
    print_time(f'reading in df from file {filename}')
    df = pd.read_csv(filename)
    return df

def infile_exists(filename: str) -> bool:
    import glob
    files = glob.glob(filename)
    if len(files) == 1:
        return True
    else:
        return False

if __name__ == '__main__':
    pass