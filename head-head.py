from bs4 import BeautifulSoup
import urllib.request
import re
import csv
import os

csv_filename = 'cache/NL-standings.csv'
os.makedirs(os.path.dirname(csv_filename), exist_ok=True)

year = '2024'
url = 'http://espn.go.com/mlb/standings/grid/_/year/' + year

page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read(), 'html.parser')

# Extracts the table for the National League (NL) and the rows for each team
NL_table = soup.find(string=re.compile("National")).find_parent("table")
NL_rows = NL_table.find_all('tr', class_=re.compile("team"))

# Creates a list of the NL teams and then appends AL for American League
NL_teams = [team_row.find('b').text for team_row in NL_rows]
NL_teams.append("AL")

# Opens a CSV file for the NL standings
with open(csv_filename, 'w', newline='') as f:
    csv_out = csv.writer(f)
    csv_out.writerow(['Team', 'Opponent', 'Wins', 'Losses'])
    
    # For each team in the NL table, identifies the team's name, the opponent,
    # and their wins and losses (WL) against that opponent. Then outputs the
    # results to the open CSV file
    for team_row in NL_rows:
        team = team_row.find('b').text
        
        # A cell has the following form:
        # <td align="right">
        # 7-9</td>
        WL_cells = team_row.find_all('td', align="right")
        
        # Extracts the values for both wins and losses from each WL table cell
        wins_losses = [td_cell.text.strip('\n').split('-') for td_cell in WL_cells]
        
        # Writes the current team's standings to the CSV file
        for i, opponent in enumerate(NL_teams):
            if team != opponent and i < len(wins_losses):
                csv_out.writerow([team, opponent, wins_losses[i][0], wins_losses[i][1]])

