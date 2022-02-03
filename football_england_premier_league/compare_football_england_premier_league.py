import pandas as pd
import numpy as np
brokers = []

betfirst = pd.read_csv('football_england_premier_league\\betfirst_football_england_premier_league.csv')

betfirst["Home_team_win"] = betfirst["Home_team_win"].astype(np.float64)
betfirst = betfirst["Home_team_win"].replace({",": "."}, inplace=True)
#betfirst = betfirst.astype({"Home_team_win": float, "Draw": float, "Away_team_win": float})
#brokers.append(betfirst)

# betway = pd.read_csv('football_england_premier_league\\betway_football_england_premier_league.csv')
# betway = betway["Home_team_win"].replace({",": "."}, inplace=True)
# betway = betway.astype({"Home_team_win": float, "Draw": float, "Away_team_win": float})
# brokers.append(betway)

# bwin = pd.read_csv('football_england_premier_league\\bwin_football_england_premier_league.csv')
# bwin = bwin.astype({"Home_team_win": float, "Draw": float, "Away_team_win": float})
# brokers.append(bwin)

# circus = pd.read_csv('football_england_premier_league\\circus_football_england_premier_league.csv')
# circus = circus.astype({"Home_team_win": float, "Draw": float, "Away_team_win": float})
# brokers.append(circus)

# ladbrokes = pd.read_csv('football_england_premier_league\\ladbrokes_football_england_premier_league.csv')
# ladbrokes = ladbrokes.astype({"Home_team_win": float, "Draw": float, "Away_team_win": float})
# brokers.append(ladbrokes)

# napoleon = pd.read_csv('football_england_premier_league\\napoleon_football_england_premier_league.csv')
# napoleon = napoleon.astype({"Home_team_win": float, "Draw": float, "Away_team_win": float})
# brokers.append(napoleon)

# pinnacle = pd.read_csv('football_england_premier_league\\pinnacle_football_england_premier_league.csv')
# pinnacle = pinnacle.astype({"Home_team_win": float, "Draw": float, "Away_team_win": float})
# brokers.append(pinnacle)

# unibet = pd.read_csv('football_england_premier_league\\unibet_football_england_premier_league.csv')
# unibet = unibet.astype({"Home_team_win": float, "Draw": float, "Away_team_win": float})
# brokers.append(unibet)

# print(brokers)

print(betfirst.head(4))
# print("*"*50)
# print(betway.head(4))
# print("*"*50)
# print(bwin.head(4))
# print("*"*50)
# print(circus.head(4))
# print("*"*50)
# print(ladbrokes.head(4))
# print("*"*50)
# print(napoleon.head(4))
# print("*"*50)
# print(pinnacle.head(4))
# print("*"*50)
# print(unibet.head(4))

# for i in range(19):
# for i in range(len(brokers)):
#     max_value_home_win = 0
#     max_value_draw = 0
#     max_value_away_win = 0
#     if brokers[i]['Home_team_win'] > max_value_home_win:
#         max_value_home_win = brokers[i]['Home_team_win']

# print(max_value_home_win)
