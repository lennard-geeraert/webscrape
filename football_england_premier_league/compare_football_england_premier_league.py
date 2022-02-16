import pandas as pd
import numpy as np

brokers = []

betfirst = pd.read_csv('football_england_premier_league\\betfirst_football_england_premier_league.csv')
betfirst['broker'] = 'betfirst'
betway = pd.read_csv('football_england_premier_league\\betway_football_england_premier_league.csv')
betway['broker'] = 'betway'
bwin = pd.read_csv('football_england_premier_league\\bwin_football_england_premier_league.csv')
bwin['broker'] = 'bwin'
circus = pd.read_csv('football_england_premier_league\\circus_football_england_premier_league.csv')
circus['broker'] = 'circus'
ladbrokes = pd.read_csv('football_england_premier_league\\ladbrokes_football_england_premier_league.csv')
ladbrokes['broker'] = 'ladbrokes'
napoleon = pd.read_csv('football_england_premier_league\\napoleon_football_england_premier_league.csv')
napoleon['broker'] = 'napoleon'
pinnacle = pd.read_csv('football_england_premier_league\\pinnacle_football_england_premier_league.csv')
pinnacle['broker'] = 'pinnacle'
unibet = pd.read_csv('football_england_premier_league\\unibet_football_england_premier_league.csv')
unibet['broker'] = 'unibet'

brokers.extend([betfirst, betway, bwin, circus, ladbrokes, napoleon, pinnacle, unibet])

for x, broker in enumerate(brokers):
    for i in range(broker.shape[0]):
        # split is optioneel als je alles wilt, maar ook meer risico
        broker["Home_team"][i] = broker["Home_team"][i].lower().replace("fc", "").strip().split(" ")[0]
        broker["Away_team"][i] = broker["Away_team"][i].lower().replace("fc", "").strip().split(" ")[0]

        if(broker["Home_team_win"].dtype != np.number):
            broker["Home_team_win"][i] = broker["Home_team_win"][i].replace(",", ".")
            broker["Draw"][i] = broker["Draw"][i].replace(",", ".")
            broker["Away_team_win"][i] = broker["Away_team_win"][i].replace(",", ".")

            broker["Home_team_win"][i] = float(broker["Home_team_win"][i])
            broker["Draw"][i] = float(broker["Draw"][i])
            broker["Away_team_win"][i] = float(broker["Away_team_win"][i])

maxLines = 0
maxLineBroker = pd.DataFrame()

for i, broker in enumerate(brokers):
    if(broker.shape[0] > maxLines):
        maxLines = broker.shape[0]
        maxLineBroker = broker

arbitrages = []
count = 0

for x in range(maxLines):
    max_value_home_win = 0
    broker_max_value_home_win = ''
    max_value_draw = 0
    broker_max_value_draw = ''
    max_value_away_win = 0
    broker_max_value_away_win = ''
    home_team = maxLineBroker['Home_team'][x]
    away_team = maxLineBroker['Away_team'][x]
    games = []

    for i, broker in enumerate(brokers):
        game = broker[(broker['Home_team'] == home_team) & (broker['Away_team'] == away_team)]
        if(game.empty == False):
            games.append(game)

    for i, game in enumerate(games):
        if(game.iloc[0]['Home_team_win'] > max_value_home_win):
            max_value_home_win = game.iloc[0]['Home_team_win']
            broker_max_value_home_win = game.iloc[0]['broker']
        if(game.iloc[0]["Away_team_win"] > max_value_away_win):
            max_value_away_win = game.iloc[0]['Away_team_win']
            broker_max_value_away_win = game.iloc[0]['broker']
        if(game.iloc[0]["Draw"] > max_value_draw):
            max_value_draw = game.iloc[0]["Draw"]
            broker_max_value_draw = game.iloc[0]['broker']

    arbitrage = 1 / max_value_home_win + 1 / max_value_draw + 1 / max_value_away_win
    arbitrages.append(arbitrage)
    print(f'Game: {home_team} VS {away_team}')
    print(f'Home team ({home_team}): {broker_max_value_home_win} & {max_value_home_win}')
    print(f'Draw: {broker_max_value_draw} & {max_value_draw}')
    print(f'Away team ({away_team}): {broker_max_value_away_win} & {max_value_away_win}')
    print(f'===>>> {arbitrage}')
    print('\n')
    count += 1

print(count)
